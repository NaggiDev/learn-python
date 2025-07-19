"""
Concurrent Web Scraper Package

A comprehensive web scraping library that demonstrates different concurrency approaches
including threading, multiprocessing, and asyncio.
"""

from .models import (
    ScrapedContent,
    ScrapingResult,
    ScrapingConfig,
    ScrapingMethod,
    PerformanceMetrics
)

from .base_scraper import BaseScraper
from .threading_scraper import ThreadingScraper
from .asyncio_scraper import AsyncioScraper

from .utils import (
    load_config,
    save_results,
    print_results,
    print_detailed_results,
    validate_urls,
    create_sample_urls,
    estimate_scraping_time,
    format_duration,
    analyze_performance
)

__version__ = "1.0.0"
__author__ = "Python Learning Path"
__description__ = "Concurrent web scraper demonstrating threading, multiprocessing, and asyncio"

__all__ = [
    # Models
    'ScrapedContent',
    'ScrapingResult', 
    'ScrapingConfig',
    'ScrapingMethod',
    'PerformanceMetrics',
    
    # Scrapers
    'BaseScraper',
    'ThreadingScraper',
    'AsyncioScraper',
    
    # Utilities
    'load_config',
    'save_results',
    'print_results',
    'print_detailed_results',
    'validate_urls',
    'create_sample_urls',
    'estimate_scraping_time',
    'format_duration',
    'analyze_performance'
]