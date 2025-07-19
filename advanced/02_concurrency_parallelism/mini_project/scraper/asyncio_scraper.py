"""
Asyncio-based web scraper implementation.
"""

import asyncio
import time
from typing import List
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from .base_scraper import BaseScraper
from .models import ScrapedContent, ScrapingResult, ScrapingConfig, ScrapingMethod


class AsyncioScraper(BaseScraper):
    """Web scraper using asyncio for concurrent requests"""
    
    def __init__(self, config: ScrapingConfig):
        super().__init__(config)
        self.semaphore = None  # Will be created in async context
    
    def get_method(self) -> ScrapingMethod:
        """Return the scraping method"""
        return ScrapingMethod.ASYNCIO
    
    def scrape_urls(self, urls: List[str]) -> ScrapingResult:
        """Scrape multiple URLs using asyncio (sync wrapper)"""
        return asyncio.run(self.async_scrape_urls(urls))
    
    async def async_scrape_urls(self, urls: List[str]) -> ScrapingResult:
        """Scrape multiple URLs using asyncio"""
        self.logger.info(f"Starting asyncio scraper for {len(urls)} URLs")
        start_time = time.time()
        
        # Create semaphore for rate limiting
        self.semaphore = asyncio.Semaphore(self.config.max_workers)
        
        # Create aiohttp session
        timeout = aiohttp.ClientTimeout(total=self.config.timeout)
        connector = aiohttp.TCPConnector(limit=self.config.max_workers * 2)
        
        async with aiohttp.ClientSession(
            timeout=timeout,
            connector=connector,
            headers={'User-Agent': self.config.user_agent}
        ) as session:
            
            # Create tasks for all URLs
            tasks = [self._scrape_with_rate_limit(session, url) for url in urls]
            
            # Execute all tasks concurrently
            content_list = await asyncio.gather(*tasks, return_exceptions=True)
            
            # Handle exceptions
            processed_content = []
            for i, content in enumerate(content_list):
                if isinstance(content, Exception):
                    self.logger.error(f"Exception for {urls[i]}: {str(content)}")
                    processed_content.append(ScrapedContent(url=urls[i], error=str(content)))
                else:
                    processed_content.append(content)
                    if content.is_successful:
                        self.logger.info(f"✓ Scraped {content.url} ({content.response_time:.2f}s)")
                    else:
                        self.logger.warning(f"✗ Failed {content.url}: {content.error}")
        
        total_time = time.time() - start_time
        result = self._create_result(processed_content, total_time)
        
        self.logger.info(f"Asyncio scraper completed: {result.successful}/{result.total_urls} "
                        f"successful in {total_time:.2f}s")
        
        return result
    
    async def _scrape_with_rate_limit(self, session: aiohttp.ClientSession, url: str) -> ScrapedContent:
        """Scrape a single URL with rate limiting"""
        async with self.semaphore:
            # Apply rate limiting
            if self.config.rate_limit > 0:
                await asyncio.sleep(self.config.rate_limit)
            
            return await self._async_scrape_single_url(session, url)
    
    async def _async_scrape_single_url(self, session: aiohttp.ClientSession, url: str) -> ScrapedContent:
        """Scrape a single URL asynchronously with retry logic"""
        for attempt in range(self.config.retries + 1):
            try:
                start_time = time.time()
                
                async with session.get(url) as response:
                    response_time = time.time() - start_time
                    
                    # Create ScrapedContent object
                    content = ScrapedContent(
                        url=url,
                        status_code=response.status,
                        response_time=response_time
                    )
                    
                    # Check if response is successful
                    if response.status == 200:
                        # Read response content
                        html_content = await response.text()
                        
                        # Extract content
                        await self._async_extract_content(content, html_content, response)
                        self.logger.debug(f"Successfully scraped {url}")
                        return content
                    else:
                        content.error = f"HTTP {response.status}"
                        self.logger.warning(f"HTTP {response.status} for {url}")
                        return content
                        
            except asyncio.TimeoutError:
                error_msg = f"Timeout after {self.config.timeout}s"
                self.logger.warning(f"Attempt {attempt + 1}: {error_msg} for {url}")
                if attempt == self.config.retries:
                    return ScrapedContent(url=url, error=error_msg)
                    
            except aiohttp.ClientError as e:
                error_msg = f"Client error: {str(e)}"
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
                await asyncio.sleep(wait_time)
        
        return ScrapedContent(url=url, error="Max retries exceeded")
    
    async def _async_extract_content(self, content: ScrapedContent, html_content: str, response):
        """Extract content from HTML asynchronously"""
        try:
            # Parse HTML content
            soup = BeautifulSoup(html_content, 'html.parser')
            
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
                'content_length': len(html_content),
                'final_url': str(response.url)  # In case of redirects
            }
            
        except Exception as e:
            self.logger.error(f"Error extracting content from {content.url}: {str(e)}")
            content.error = f"Content extraction error: {str(e)}"


class AsyncioScraperWithBatching(AsyncioScraper):
    """Asyncio scraper that processes URLs in batches"""
    
    def __init__(self, config: ScrapingConfig, batch_size: int = 10):
        super().__init__(config)
        self.batch_size = batch_size
    
    async def async_scrape_urls(self, urls: List[str]) -> ScrapingResult:
        """Scrape URLs in batches to manage memory and connections"""
        self.logger.info(f"Starting batched asyncio scraper for {len(urls)} URLs "
                        f"(batch size: {self.batch_size})")
        
        start_time = time.time()
        all_content = []
        
        # Process URLs in batches
        for i in range(0, len(urls), self.batch_size):
            batch_urls = urls[i:i + self.batch_size]
            self.logger.info(f"Processing batch {i // self.batch_size + 1} "
                           f"({len(batch_urls)} URLs)")
            
            batch_result = await super().async_scrape_urls(batch_urls)
            all_content.extend(batch_result.content)
            
            # Small delay between batches
            if i + self.batch_size < len(urls):
                await asyncio.sleep(0.1)
        
        total_time = time.time() - start_time
        result = self._create_result(all_content, total_time)
        
        self.logger.info(f"Batched asyncio scraper completed: {result.successful}/{result.total_urls} "
                        f"successful in {total_time:.2f}s")
        
        return result


class AsyncioScraperWithProgress(AsyncioScraper):
    """Asyncio scraper with progress reporting"""
    
    def __init__(self, config: ScrapingConfig):
        super().__init__(config)
        self.completed_count = 0
        self.progress_callback = None
        self.progress_lock = asyncio.Lock()
    
    def set_progress_callback(self, callback):
        """Set a callback function for progress updates"""
        self.progress_callback = callback
    
    async def _scrape_with_rate_limit(self, session: aiohttp.ClientSession, url: str) -> ScrapedContent:
        """Scrape with progress tracking"""
        content = await super()._scrape_with_rate_limit(session, url)
        
        # Update progress
        if self.progress_lock:
            async with self.progress_lock:
                self.completed_count += 1
                if self.progress_callback:
                    await self.progress_callback(self.completed_count, self.total_urls)
        
        return content
    
    async def async_scrape_urls(self, urls: List[str]) -> ScrapingResult:
        """Scrape with progress tracking"""
        self.completed_count = 0
        self.total_urls = len(urls)
        return await super().async_scrape_urls(urls)


# Example usage and testing
if __name__ == "__main__":
    import json
    
    async def main():
        # Load configuration
        config = ScrapingConfig(
            max_workers=5,
            rate_limit=0.2,
            timeout=10,
            retries=2
        )
        
        # Test URLs
        test_urls = [
            "https://httpbin.org/html",
            "https://httpbin.org/json",
            "https://httpbin.org/delay/1",
            "https://httpbin.org/delay/2",
            "https://httpbin.org/status/200",
            "https://httpbin.org/status/404",  # This will fail
            "https://httpbin.org/headers"
        ]
        
        # Test basic asyncio scraper
        print("Testing AsyncioScraper...")
        scraper = AsyncioScraper(config)
        result = await scraper.async_scrape_urls(test_urls)
        
        print(f"Results: {result.successful}/{result.total_urls} successful")
        print(f"Total time: {result.total_time:.2f}s")
        print(f"Average response time: {result.average_response_time:.2f}s")
        print(f"URLs per second: {result.urls_per_second:.2f}")
        
        # Test batched scraper
        print("\nTesting AsyncioScraperWithBatching...")
        batch_scraper = AsyncioScraperWithBatching(config, batch_size=3)
        batch_result = await batch_scraper.async_scrape_urls(test_urls)
        
        print(f"Batched results: {batch_result.successful}/{batch_result.total_urls} successful")
        print(f"Total time: {batch_result.total_time:.2f}s")
        
        # Save results to file
        with open('asyncio_results.json', 'w') as f:
            json.dump(result.to_dict(), f, indent=2)
        
        return result
    
    # Run the async main function
    asyncio.run(main())