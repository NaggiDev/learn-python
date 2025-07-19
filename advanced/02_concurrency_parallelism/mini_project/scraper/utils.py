"""
Utility functions for the web scraper project.
"""

import json
import time
from pathlib import Path
from typing import Dict, Any, List
import logging

from .models import ScrapingConfig, ScrapingResult


def load_config(config_file: str) -> ScrapingConfig:
    """Load configuration from JSON file"""
    try:
        with open(config_file, 'r') as f:
            config_dict = json.load(f)
        return ScrapingConfig.from_dict(config_dict)
    except FileNotFoundError:
        logging.error(f"Configuration file '{config_file}' not found")
        return ScrapingConfig()  # Return default config
    except json.JSONDecodeError as e:
        logging.error(f"Error parsing configuration file: {e}")
        return ScrapingConfig()


def save_results(data: Dict[str, Any], output_file: str):
    """Save results to JSON file"""
    try:
        # Create output directory if it doesn't exist
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2, default=str)
        
        logging.info(f"Results saved to {output_file}")
    except Exception as e:
        logging.error(f"Error saving results: {e}")


def print_results(result: ScrapingResult):
    """Print scraping results in a formatted way"""
    print(f"\nScraping Results ({result.method.value}):")
    print("-" * 40)
    print(f"Total URLs: {result.total_urls}")
    print(f"Successful: {result.successful}")
    print(f"Failed: {result.failed}")
    print(f"Success Rate: {result.success_rate:.1f}%")
    print(f"Total Time: {result.total_time:.2f}s")
    print(f"URLs per Second: {result.urls_per_second:.2f}")
    print(f"Average Response Time: {result.average_response_time:.3f}s")
    
    if result.errors:
        print(f"\nErrors ({len(result.errors)}):")
        for error in result.errors[:5]:  # Show first 5 errors
            print(f"  - {error}")
        if len(result.errors) > 5:
            print(f"  ... and {len(result.errors) - 5} more")


def print_detailed_results(result: ScrapingResult):
    """Print detailed results including individual URL results"""
    print_results(result)
    
    print(f"\nDetailed Results:")
    print("-" * 60)
    print(f"{'URL':<40} {'Status':<8} {'Time(s)':<8} {'Title':<20}")
    print("-" * 60)
    
    for content in result.content:
        status = "✓" if content.is_successful else "✗"
        title = (content.title[:17] + "...") if content.title and len(content.title) > 20 else (content.title or "")
        url_display = content.url[:37] + "..." if len(content.url) > 40 else content.url
        
        print(f"{url_display:<40} {status:<8} {content.response_time:<8.3f} {title:<20}")


def create_sample_urls() -> List[str]:
    """Create a list of sample URLs for testing"""
    return [
        "https://httpbin.org/html",
        "https://httpbin.org/json",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/status/200",
        "https://httpbin.org/status/404",
        "https://httpbin.org/headers",
        "https://httpbin.org/user-agent",
        "https://httpbin.org/ip",
        "https://httpbin.org/uuid"
    ]


def validate_urls(urls: List[str]) -> List[str]:
    """Validate and filter URLs"""
    valid_urls = []
    for url in urls:
        url = url.strip()
        if url and (url.startswith('http://') or url.startswith('https://')):
            valid_urls.append(url)
        else:
            logging.warning(f"Invalid URL skipped: {url}")
    
    return valid_urls


def estimate_scraping_time(num_urls: int, config: ScrapingConfig) -> float:
    """Estimate scraping time based on configuration"""
    # Simple estimation: assume average response time of 1 second
    # and account for rate limiting and concurrency
    avg_response_time = 1.0
    rate_limit_overhead = config.rate_limit
    
    # Time per batch of concurrent requests
    time_per_batch = max(avg_response_time, rate_limit_overhead)
    
    # Number of batches needed
    num_batches = (num_urls + config.max_workers - 1) // config.max_workers
    
    estimated_time = num_batches * time_per_batch
    return estimated_time


def format_duration(seconds: float) -> str:
    """Format duration in human-readable format"""
    if seconds < 60:
        return f"{seconds:.1f}s"
    elif seconds < 3600:
        minutes = int(seconds // 60)
        remaining_seconds = seconds % 60
        return f"{minutes}m {remaining_seconds:.1f}s"
    else:
        hours = int(seconds // 3600)
        remaining_minutes = int((seconds % 3600) // 60)
        return f"{hours}h {remaining_minutes}m"


def create_progress_callback(total_urls: int):
    """Create a progress callback function"""
    start_time = time.time()
    
    def progress_callback(completed: int, total: int = None):
        if total is None:
            total = total_urls
        
        percentage = (completed / total) * 100
        elapsed_time = time.time() - start_time
        
        if completed > 0:
            estimated_total_time = elapsed_time * (total / completed)
            remaining_time = estimated_total_time - elapsed_time
            
            print(f"\rProgress: {completed}/{total} ({percentage:.1f}%) "
                  f"- Elapsed: {format_duration(elapsed_time)} "
                  f"- Remaining: {format_duration(remaining_time)}", end="")
        else:
            print(f"\rProgress: {completed}/{total} ({percentage:.1f}%)", end="")
        
        if completed == total:
            print()  # New line when complete
    
    return progress_callback


def analyze_performance(results: Dict[str, ScrapingResult]) -> Dict[str, Any]:
    """Analyze performance across different scraping methods"""
    analysis = {
        'summary': {},
        'comparison': {},
        'recommendations': []
    }
    
    if not results:
        return analysis
    
    # Calculate summary statistics
    methods = list(results.keys())
    times = [result.total_time for result in results.values()]
    success_rates = [result.success_rate for result in results.values()]
    urls_per_second = [result.urls_per_second for result in results.values()]
    
    analysis['summary'] = {
        'fastest_method': methods[times.index(min(times))],
        'slowest_method': methods[times.index(max(times))],
        'best_success_rate': methods[success_rates.index(max(success_rates))],
        'highest_throughput': methods[urls_per_second.index(max(urls_per_second))]
    }
    
    # Performance comparison
    baseline_time = min(times)
    for method, result in results.items():
        speedup = baseline_time / result.total_time if result.total_time > 0 else 0
        analysis['comparison'][method] = {
            'speedup_factor': speedup,
            'relative_performance': 'baseline' if result.total_time == baseline_time else f"{speedup:.2f}x slower"
        }
    
    # Generate recommendations
    fastest = analysis['summary']['fastest_method']
    highest_throughput = analysis['summary']['highest_throughput']
    
    if fastest == highest_throughput:
        analysis['recommendations'].append(f"Use {fastest} for best overall performance")
    else:
        analysis['recommendations'].append(f"Use {fastest} for fastest completion")
        analysis['recommendations'].append(f"Use {highest_throughput} for highest throughput")
    
    # Add specific recommendations based on results
    for method, result in results.items():
        if result.success_rate < 90:
            analysis['recommendations'].append(f"Consider increasing retries for {method} (current success rate: {result.success_rate:.1f}%)")
        
        if result.urls_per_second < 1:
            analysis['recommendations'].append(f"Consider reducing rate limit for {method} to improve throughput")
    
    return analysis


# Example usage and testing
if __name__ == "__main__":
    # Test utility functions
    print("Testing utility functions...")
    
    # Test URL validation
    test_urls = [
        "https://example.com",
        "http://test.com",
        "invalid-url",
        "",
        "ftp://files.com"
    ]
    
    valid_urls = validate_urls(test_urls)
    print(f"Valid URLs: {valid_urls}")
    
    # Test time estimation
    config = ScrapingConfig(max_workers=5, rate_limit=0.5)
    estimated_time = estimate_scraping_time(20, config)
    print(f"Estimated time for 20 URLs: {format_duration(estimated_time)}")
    
    # Test progress callback
    progress = create_progress_callback(10)
    for i in range(11):
        progress(i)
        time.sleep(0.1)
    
    print("Utility functions test completed!")