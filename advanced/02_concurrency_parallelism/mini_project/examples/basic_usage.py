#!/usr/bin/env python3
"""
Basic usage examples for the concurrent web scraper.

This script demonstrates how to use the different scraper implementations
with simple examples.
"""

import sys
import asyncio
from pathlib import Path

# Add the parent directory to the path to import the scraper package
sys.path.append(str(Path(__file__).parent.parent))

from scraper import (
    ScrapingConfig,
    ThreadingScraper,
    AsyncioScraper,
    create_sample_urls,
    print_results
)


def example_1_basic_threading():
    """Example 1: Basic threading scraper usage"""
    print("="*60)
    print("EXAMPLE 1: Basic Threading Scraper")
    print("="*60)
    
    # Create configuration
    config = ScrapingConfig(
        max_workers=3,
        rate_limit=0.5,
        timeout=10,
        retries=2,
        extract_title=True,
        extract_links=False
    )
    
    # Sample URLs
    urls = [
        "https://httpbin.org/html",
        "https://httpbin.org/json", 
        "https://httpbin.org/delay/1",
        "https://httpbin.org/status/200"
    ]
    
    # Create and run scraper
    scraper = ThreadingScraper(config)
    result = scraper.scrape_urls(urls)
    
    # Print results
    print_results(result)
    
    # Show some scraped content
    print("\nSample scraped content:")
    for content in result.content[:2]:  # Show first 2
        print(f"URL: {content.url}")
        print(f"Title: {content.title}")
        print(f"Status: {content.status_code}")
        print(f"Response time: {content.response_time:.3f}s")
        print("-" * 40)


async def example_2_basic_asyncio():
    """Example 2: Basic asyncio scraper usage"""
    print("\n" + "="*60)
    print("EXAMPLE 2: Basic Asyncio Scraper")
    print("="*60)
    
    # Create configuration
    config = ScrapingConfig(
        max_workers=5,
        rate_limit=0.2,
        timeout=10,
        retries=2,
        extract_title=True,
        extract_links=True
    )
    
    # Sample URLs
    urls = [
        "https://httpbin.org/html",
        "https://httpbin.org/json",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/headers"
    ]
    
    # Create and run scraper
    scraper = AsyncioScraper(config)
    result = await scraper.async_scrape_urls(urls)
    
    # Print results
    print_results(result)
    
    # Show some scraped content
    print("\nSample scraped content:")
    for content in result.content[:2]:  # Show first 2
        print(f"URL: {content.url}")
        print(f"Title: {content.title}")
        print(f"Links found: {len(content.links)}")
        print(f"Status: {content.status_code}")
        print(f"Response time: {content.response_time:.3f}s")
        print("-" * 40)


def example_3_configuration_options():
    """Example 3: Different configuration options"""
    print("\n" + "="*60)
    print("EXAMPLE 3: Configuration Options")
    print("="*60)
    
    # Fast configuration (high concurrency, low rate limit)
    fast_config = ScrapingConfig(
        max_workers=10,
        rate_limit=0.1,
        timeout=5,
        retries=1,
        extract_title=True,
        extract_links=False,
        extract_text=False
    )
    
    # Conservative configuration (low concurrency, higher rate limit)
    conservative_config = ScrapingConfig(
        max_workers=2,
        rate_limit=1.0,
        timeout=15,
        retries=3,
        extract_title=True,
        extract_links=True,
        extract_text=True,
        max_text_length=500
    )
    
    # Test URLs
    urls = create_sample_urls()[:5]  # Use first 5 sample URLs
    
    print("Testing FAST configuration:")
    fast_scraper = ThreadingScraper(fast_config)
    fast_result = fast_scraper.scrape_urls(urls)
    print(f"Fast config: {fast_result.total_time:.2f}s, {fast_result.urls_per_second:.2f} URLs/s")
    
    print("\nTesting CONSERVATIVE configuration:")
    conservative_scraper = ThreadingScraper(conservative_config)
    conservative_result = conservative_scraper.scrape_urls(urls)
    print(f"Conservative config: {conservative_result.total_time:.2f}s, {conservative_result.urls_per_second:.2f} URLs/s")
    
    # Compare results
    print(f"\nComparison:")
    print(f"Fast config was {conservative_result.total_time / fast_result.total_time:.2f}x faster")
    print(f"But conservative config extracted more data per URL")


def example_4_error_handling():
    """Example 4: Error handling and failed requests"""
    print("\n" + "="*60)
    print("EXAMPLE 4: Error Handling")
    print("="*60)
    
    # Configuration with retries
    config = ScrapingConfig(
        max_workers=3,
        rate_limit=0.3,
        timeout=5,
        retries=2
    )
    
    # URLs with some that will fail
    urls = [
        "https://httpbin.org/status/200",  # Success
        "https://httpbin.org/status/404",  # Not found
        "https://httpbin.org/status/500",  # Server error
        "https://httpbin.org/delay/10",    # Will timeout
        "https://invalid-domain-that-does-not-exist.com",  # DNS error
        "https://httpbin.org/json"         # Success
    ]
    
    # Run scraper
    scraper = ThreadingScraper(config)
    result = scraper.scrape_urls(urls)
    
    # Print overall results
    print_results(result)
    
    # Show detailed error information
    print("\nDetailed results:")
    for content in result.content:
        status = "✓ SUCCESS" if content.is_successful else "✗ FAILED"
        print(f"{content.url[:50]:<50} {status}")
        if content.error:
            print(f"  Error: {content.error}")
        elif content.status_code:
            print(f"  Status: {content.status_code}, Time: {content.response_time:.3f}s")
        print()


def example_5_custom_extraction():
    """Example 5: Custom content extraction"""
    print("\n" + "="*60)
    print("EXAMPLE 5: Custom Content Extraction")
    print("="*60)
    
    # Configuration for detailed extraction
    config = ScrapingConfig(
        max_workers=3,
        rate_limit=0.5,
        extract_title=True,
        extract_links=True,
        extract_text=True,
        max_text_length=200
    )
    
    # URLs with rich content
    urls = [
        "https://httpbin.org/html",  # Has HTML content
        "https://httpbin.org/json"   # JSON response
    ]
    
    # Run scraper
    scraper = ThreadingScraper(config)
    result = scraper.scrape_urls(urls)
    
    # Show extracted content
    print("Extracted content details:")
    for content in result.content:
        print(f"\nURL: {content.url}")
        print(f"Title: {content.title}")
        print(f"Links found: {len(content.links)}")
        if content.links:
            print(f"First few links: {content.links[:3]}")
        if content.text_content:
            print(f"Text content (first 100 chars): {content.text_content[:100]}...")
        print(f"Metadata: {content.metadata}")
        print("-" * 50)


async def main():
    """Run all examples"""
    print("Concurrent Web Scraper - Basic Usage Examples")
    print("=" * 60)
    
    # Run synchronous examples
    example_1_basic_threading()
    example_3_configuration_options()
    example_4_error_handling()
    example_5_custom_extraction()
    
    # Run asynchronous example
    await example_2_basic_asyncio()
    
    print("\n" + "="*60)
    print("All examples completed!")
    print("="*60)


if __name__ == "__main__":
    # Run the examples
    asyncio.run(main())