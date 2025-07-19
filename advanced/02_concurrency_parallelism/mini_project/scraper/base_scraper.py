"""
Base scraper class with common functionality.
"""

import time
import logging
from abc import ABC, abstractmethod
from typing import List, Optional
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup

from .models import ScrapedContent, ScrapingResult, ScrapingConfig, ScrapingMethod


class BaseScraper(ABC):
    """Abstract base class for all scrapers"""
    
    def __init__(self, config: ScrapingConfig):
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)
        self._setup_logging()
    
    def _setup_logging(self):
        """Set up logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    
    @abstractmethod
    def scrape_urls(self, urls: List[str]) -> ScrapingResult:
        """Abstract method to scrape multiple URLs"""
        pass
    
    @abstractmethod
    def get_method(self) -> ScrapingMethod:
        """Return the scraping method used by this scraper"""
        pass
    
    def scrape_single_url(self, url: str, session=None) -> ScrapedContent:
        """
        Scrape a single URL with retry logic.
        This method can be used by all concrete implementations.
        """
        for attempt in range(self.config.retries + 1):
            try:
                start_time = time.time()
                
                # Use provided session or create a new one
                if session:
                    response = session.get(
                        url,
                        timeout=self.config.timeout,
                        headers={'User-Agent': self.config.user_agent}
                    )
                else:
                    response = requests.get(
                        url,
                        timeout=self.config.timeout,
                        headers={'User-Agent': self.config.user_agent}
                    )
                
                response_time = time.time() - start_time
                
                # Create ScrapedContent object
                content = ScrapedContent(
                    url=url,
                    status_code=response.status_code,
                    response_time=response_time
                )
                
                # Check if response is successful
                if response.status_code == 200:
                    # Extract content based on configuration
                    self._extract_content(content, response)
                    self.logger.debug(f"Successfully scraped {url}")
                    return content
                else:
                    content.error = f"HTTP {response.status_code}"
                    self.logger.warning(f"HTTP {response.status_code} for {url}")
                    return content
                    
            except requests.exceptions.Timeout:
                error_msg = f"Timeout after {self.config.timeout}s"
                self.logger.warning(f"Attempt {attempt + 1}: {error_msg} for {url}")
                if attempt == self.config.retries:
                    return ScrapedContent(url=url, error=error_msg)
                    
            except requests.exceptions.ConnectionError:
                error_msg = "Connection error"
                self.logger.warning(f"Attempt {attempt + 1}: {error_msg} for {url}")
                if attempt == self.config.retries:
                    return ScrapedContent(url=url, error=error_msg)
                    
            except Exception as e:
                error_msg = f"Unexpected error: {str(e)}"
                self.logger.error(f"Attempt {attempt + 1}: {error_msg} for {url}")
                if attempt == self.config.retries:
                    return ScrapedContent(url=url, error=error_msg)
            
            # Wait before retry (exponential backoff)
            if attempt < self.config.retries:
                wait_time = (2 ** attempt) * 0.5
                time.sleep(wait_time)
        
        # This should never be reached, but just in case
        return ScrapedContent(url=url, error="Max retries exceeded")
    
    def _extract_content(self, content: ScrapedContent, response: requests.Response):
        """Extract content from HTTP response based on configuration"""
        try:
            # Parse HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract title
            if self.config.extract_title:
                title_tag = soup.find('title')
                if title_tag:
                    content.title = title_tag.get_text().strip()
            
            # Extract links
            if self.config.extract_links:
                links = []
                for link_tag in soup.find_all('a', href=True):
                    href = link_tag['href']
                    # Convert relative URLs to absolute
                    absolute_url = urljoin(content.url, href)
                    links.append(absolute_url)
                content.links = links
            
            # Extract text content
            if self.config.extract_text:
                # Remove script and style elements
                for script in soup(["script", "style"]):
                    script.decompose()
                
                # Get text content
                text = soup.get_text()
                # Clean up whitespace
                lines = (line.strip() for line in text.splitlines())
                chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                text = ' '.join(chunk for chunk in chunks if chunk)
                
                # Limit text length
                if len(text) > self.config.max_text_length:
                    text = text[:self.config.max_text_length] + "..."
                
                content.text_content = text
            
            # Add metadata
            content.metadata = {
                'content_type': response.headers.get('content-type', ''),
                'content_length': len(response.content),
                'encoding': response.encoding,
                'final_url': response.url  # In case of redirects
            }
            
        except Exception as e:
            self.logger.error(f"Error extracting content from {content.url}: {str(e)}")
            content.error = f"Content extraction error: {str(e)}"
    
    def _create_result(self, content_list: List[ScrapedContent], total_time: float) -> ScrapingResult:
        """Create a ScrapingResult from a list of ScrapedContent"""
        successful = sum(1 for content in content_list if content.is_successful)
        failed = len(content_list) - successful
        
        # Calculate average response time (only for successful requests)
        successful_content = [c for c in content_list if c.is_successful]
        avg_response_time = 0.0
        if successful_content:
            avg_response_time = sum(c.response_time for c in successful_content) / len(successful_content)
        
        # Collect errors
        errors = [content.error for content in content_list if content.error]
        
        return ScrapingResult(
            method=self.get_method(),
            total_urls=len(content_list),
            successful=successful,
            failed=failed,
            total_time=total_time,
            average_response_time=avg_response_time,
            content=content_list,
            errors=errors
        )
    
    def _apply_rate_limit(self):
        """Apply rate limiting between requests"""
        if self.config.rate_limit > 0:
            time.sleep(self.config.rate_limit)