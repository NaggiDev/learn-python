"""
Threading-based web scraper implementation.
"""

import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List
import requests

from .base_scraper import BaseScraper
from .models import ScrapedContent, ScrapingResult, ScrapingConfig, ScrapingMethod


class ThreadingScraper(BaseScraper):
    """Web scraper using threading for concurrent requests"""
    
    def __init__(self, config: ScrapingConfig):
        super().__init__(config)
        self.rate_limiter = threading.Semaphore(1)  # For rate limiting
        self.session_lock = threading.Lock()
        
    def get_method(self) -> ScrapingMethod:
        """Return the scraping method"""
        return ScrapingMethod.THREADING
    
    def scrape_urls(self, urls: List[str]) -> ScrapingResult:
        """Scrape multiple URLs using ThreadPoolExecutor"""
        self.logger.info(f"Starting threading scraper for {len(urls)} URLs")
        start_time = time.time()
        
        # Create a session for connection pooling
        session = requests.Session()
        session.headers.update({'User-Agent': self.config.user_agent})
        
        try:
            with ThreadPoolExecutor(max_workers=self.config.max_workers) as executor:
                # Submit all tasks
                future_to_url = {
                    executor.submit(self._scrape_with_rate_limit, url, session): url 
                    for url in urls
                }
                
                # Collect results as they complete
                content_list = []
                for future in as_completed(future_to_url):
                    url = future_to_url[future]
                    try:
                        content = future.result()
                        content_list.append(content)
                        
                        if content.is_successful:
                            self.logger.info(f"✓ Scraped {url} ({content.response_time:.2f}s)")
                        else:
                            self.logger.warning(f"✗ Failed {url}: {content.error}")
                            
                    except Exception as e:
                        self.logger.error(f"Exception for {url}: {str(e)}")
                        content_list.append(ScrapedContent(url=url, error=str(e)))
        
        finally:
            session.close()
        
        total_time = time.time() - start_time
        result = self._create_result(content_list, total_time)
        
        self.logger.info(f"Threading scraper completed: {result.successful}/{result.total_urls} "
                        f"successful in {total_time:.2f}s")
        
        return result
    
    def _scrape_with_rate_limit(self, url: str, session: requests.Session) -> ScrapedContent:
        """Scrape a single URL with rate limiting"""
        # Apply rate limiting
        with self.rate_limiter:
            if self.config.rate_limit > 0:
                time.sleep(self.config.rate_limit)
        
        # Scrape the URL
        return self.scrape_single_url(url, session)


class AdvancedThreadingScraper(ThreadingScraper):
    """Advanced threading scraper with additional features"""
    
    def __init__(self, config: ScrapingConfig):
        super().__init__(config)
        self.progress_lock = threading.Lock()
        self.completed_count = 0
        self.progress_callback = None
    
    def set_progress_callback(self, callback):
        """Set a callback function for progress updates"""
        self.progress_callback = callback
    
    def scrape_urls(self, urls: List[str]) -> ScrapingResult:
        """Scrape URLs with progress tracking"""
        self.completed_count = 0
        return super().scrape_urls(urls)
    
    def _scrape_with_rate_limit(self, url: str, session: requests.Session) -> ScrapedContent:
        """Scrape with progress tracking"""
        content = super()._scrape_with_rate_limit(url, session)
        
        # Update progress
        with self.progress_lock:
            self.completed_count += 1
            if self.progress_callback:
                self.progress_callback(self.completed_count, len(urls))
        
        return content


class ThreadingScraperWithRetry(ThreadingScraper):
    """Threading scraper with enhanced retry mechanism"""
    
    def __init__(self, config: ScrapingConfig):
        super().__init__(config)
        self.retry_queue = []
        self.retry_lock = threading.Lock()
    
    def scrape_urls(self, urls: List[str]) -> ScrapingResult:
        """Scrape URLs with retry mechanism for failed requests"""
        # First pass
        result = super().scrape_urls(urls)
        
        # Collect failed URLs for retry
        failed_urls = [content.url for content in result.content if not content.is_successful]
        
        if failed_urls and self.config.retries > 0:
            self.logger.info(f"Retrying {len(failed_urls)} failed URLs")
            
            # Retry failed URLs with reduced concurrency
            retry_config = ScrapingConfig(
                max_workers=min(2, self.config.max_workers),
                rate_limit=self.config.rate_limit * 2,  # Slower rate for retries
                timeout=self.config.timeout * 2,  # Longer timeout
                retries=1  # Only one retry attempt
            )
            
            retry_scraper = ThreadingScraper(retry_config)
            retry_result = retry_scraper.scrape_urls(failed_urls)
            
            # Update original results with retry results
            self._merge_retry_results(result, retry_result)
        
        return result
    
    def _merge_retry_results(self, original: ScrapingResult, retry: ScrapingResult):
        """Merge retry results into original results"""
        # Create a mapping of URL to retry content
        retry_map = {content.url: content for content in retry.content}
        
        # Update original content with successful retries
        for i, content in enumerate(original.content):
            if not content.is_successful and content.url in retry_map:
                retry_content = retry_map[content.url]
                if retry_content.is_successful:
                    original.content[i] = retry_content
                    original.successful += 1
                    original.failed -= 1
                    self.logger.info(f"Retry successful for {content.url}")


# Example usage and testing
if __name__ == "__main__":
    import json
    
    # Load configuration
    config = ScrapingConfig(
        max_workers=3,
        rate_limit=0.5,
        timeout=10,
        retries=2
    )
    
    # Test URLs
    test_urls = [
        "https://httpbin.org/html",
        "https://httpbin.org/json",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/status/200",
        "https://httpbin.org/status/404"  # This will fail
    ]
    
    # Test basic threading scraper
    print("Testing ThreadingScraper...")
    scraper = ThreadingScraper(config)
    result = scraper.scrape_urls(test_urls)
    
    print(f"Results: {result.successful}/{result.total_urls} successful")
    print(f"Total time: {result.total_time:.2f}s")
    print(f"Average response time: {result.average_response_time:.2f}s")
    
    # Test advanced scraper with retry
    print("\nTesting ThreadingScraperWithRetry...")
    retry_scraper = ThreadingScraperWithRetry(config)
    retry_result = retry_scraper.scrape_urls(test_urls)
    
    print(f"Results: {retry_result.successful}/{retry_result.total_urls} successful")
    print(f"Total time: {retry_result.total_time:.2f}s")
    
    # Save results to file
    with open('threading_results.json', 'w') as f:
        json.dump(result.to_dict(), f, indent=2)