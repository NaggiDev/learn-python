#!/usr/bin/env python3
"""
Main application for the concurrent web scraper.

This script provides a command-line interface to run different scraping methods
and compare their performance.
"""

import argparse
import json
import time
import sys
from pathlib import Path
from typing import List

# Add the scraper package to the path
sys.path.append(str(Path(__file__).parent))

from scraper.models import ScrapingConfig, PerformanceMetrics
from scraper.threading_scraper import ThreadingScraper
from scraper.asyncio_scraper import AsyncioScraper
from scraper.utils import load_config, save_results, print_results


def load_urls_from_file(file_path: str) -> List[str]:
    """Load URLs from a text file (one URL per line)"""
    try:
        with open(file_path, 'r') as f:
            urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        return urls
    except FileNotFoundError:
        print(f"Error: URL file '{file_path}' not found")
        return []


def load_urls_from_config(config_file: str) -> List[str]:
    """Load URLs from configuration file"""
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
        return config.get('urls', [])
    except FileNotFoundError:
        print(f"Error: Config file '{config_file}' not found")
        return []


def run_scraper(scraper_type: str, urls: List[str], config: ScrapingConfig):
    """Run a specific scraper and return results"""
    print(f"\n{'='*50}")
    print(f"Running {scraper_type.upper()} scraper")
    print(f"{'='*50}")
    
    start_time = time.time()
    
    if scraper_type == 'threading':
        scraper = ThreadingScraper(config)
        result = scraper.scrape_urls(urls)
    elif scraper_type == 'asyncio':
        scraper = AsyncioScraper(config)
        result = scraper.scrape_urls(urls)
    else:
        raise ValueError(f"Unknown scraper type: {scraper_type}")
    
    end_time = time.time()
    
    # Print results
    print_results(result)
    
    return result


def compare_scrapers(urls: List[str], config: ScrapingConfig):
    """Compare all scraper implementations"""
    print(f"\n{'='*60}")
    print("PERFORMANCE COMPARISON")
    print(f"{'='*60}")
    print(f"URLs to scrape: {len(urls)}")
    print(f"Max workers: {config.max_workers}")
    print(f"Rate limit: {config.rate_limit}s")
    
    results = {}
    metrics = []
    
    # Test each scraper type
    scraper_types = ['threading', 'asyncio']
    
    for scraper_type in scraper_types:
        try:
            result = run_scraper(scraper_type, urls, config)
            results[scraper_type] = result
            
            # Create performance metrics
            metric = PerformanceMetrics(
                method=result.method,
                total_time=result.total_time,
                urls_per_second=result.urls_per_second,
                success_rate=result.success_rate,
                average_response_time=result.average_response_time
            )
            metrics.append(metric)
            
        except Exception as e:
            print(f"Error running {scraper_type} scraper: {e}")
    
    # Print comparison summary
    print(f"\n{'='*60}")
    print("COMPARISON SUMMARY")
    print(f"{'='*60}")
    
    print(f"{'Method':<15} {'Time(s)':<10} {'URLs/s':<10} {'Success%':<10} {'Avg RT(s)':<10}")
    print("-" * 60)
    
    for metric in metrics:
        print(f"{metric.method.value:<15} "
              f"{metric.total_time:<10.2f} "
              f"{metric.urls_per_second:<10.2f} "
              f"{metric.success_rate:<10.1f} "
              f"{metric.average_response_time:<10.3f}")
    
    # Find the fastest method
    if metrics:
        fastest = min(metrics, key=lambda x: x.total_time)
        print(f"\nFastest method: {fastest.method.value} "
              f"({fastest.total_time:.2f}s, {fastest.urls_per_second:.2f} URLs/s)")
    
    return results, metrics


def main():
    """Main application entry point"""
    parser = argparse.ArgumentParser(description="Concurrent Web Scraper")
    
    # URL source options
    url_group = parser.add_mutually_exclusive_group(required=True)
    url_group.add_argument('--urls', nargs='+', help='URLs to scrape')
    url_group.add_argument('--url-file', help='File containing URLs (one per line)')
    url_group.add_argument('--config', help='Configuration file with URLs and settings')
    
    # Scraper options
    parser.add_argument('--method', choices=['threading', 'asyncio', 'all'], 
                       default='all', help='Scraping method to use')
    parser.add_argument('--workers', type=int, default=5, 
                       help='Maximum number of concurrent workers')
    parser.add_argument('--rate-limit', type=float, default=0.5,
                       help='Rate limit between requests (seconds)')
    parser.add_argument('--timeout', type=int, default=10,
                       help='Request timeout (seconds)')
    parser.add_argument('--retries', type=int, default=3,
                       help='Number of retry attempts')
    
    # Output options
    parser.add_argument('--output', help='Output file for results (JSON format)')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose logging')
    
    args = parser.parse_args()
    
    # Load URLs
    urls = []
    if args.urls:
        urls = args.urls
    elif args.url_file:
        urls = load_urls_from_file(args.url_file)
    elif args.config:
        urls = load_urls_from_config(args.config)
    
    if not urls:
        print("Error: No URLs to scrape")
        return 1
    
    print(f"Loaded {len(urls)} URLs to scrape")
    
    # Create configuration
    if args.config:
        config = load_config(args.config)
        # Override with command line arguments
        config.max_workers = args.workers
        config.rate_limit = args.rate_limit
        config.timeout = args.timeout
        config.retries = args.retries
    else:
        config = ScrapingConfig(
            max_workers=args.workers,
            rate_limit=args.rate_limit,
            timeout=args.timeout,
            retries=args.retries
        )
    
    # Run scraper(s)
    if args.method == 'all':
        results, metrics = compare_scrapers(urls, config)
        
        # Save comparison results
        if args.output:
            comparison_data = {
                'urls': urls,
                'config': config.__dict__,
                'results': {method: result.to_dict() for method, result in results.items()},
                'metrics': [metric.to_dict() for metric in metrics]
            }
            save_results(comparison_data, args.output)
            print(f"\nResults saved to {args.output}")
    
    else:
        result = run_scraper(args.method, urls, config)
        
        # Save single result
        if args.output:
            save_results(result.to_dict(), args.output)
            print(f"\nResults saved to {args.output}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())