"""
Data models for the web scraper project.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum


class ScrapingMethod(Enum):
    """Enumeration of available scraping methods"""
    THREADING = "threading"
    MULTIPROCESSING = "multiprocessing"
    ASYNCIO = "asyncio"
    SEQUENTIAL = "sequential"


@dataclass
class ScrapedContent:
    """Model for scraped content from a single URL"""
    url: str
    title: Optional[str] = None
    links: List[str] = field(default_factory=list)
    text_content: Optional[str] = None
    status_code: Optional[int] = None
    response_time: float = 0.0
    scraped_at: datetime = field(default_factory=datetime.now)
    error: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    @property
    def is_successful(self) -> bool:
        """Check if scraping was successful"""
        return self.error is None and self.status_code and 200 <= self.status_code < 300
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization"""
        return {
            'url': self.url,
            'title': self.title,
            'links': self.links,
            'text_content': self.text_content,
            'status_code': self.status_code,
            'response_time': self.response_time,
            'scraped_at': self.scraped_at.isoformat(),
            'error': self.error,
            'metadata': self.metadata,
            'is_successful': self.is_successful
        }


@dataclass
class ScrapingResult:
    """Model for overall scraping results"""
    method: ScrapingMethod
    total_urls: int
    successful: int
    failed: int
    total_time: float
    average_response_time: float
    content: List[ScrapedContent] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    @property
    def success_rate(self) -> float:
        """Calculate success rate as percentage"""
        if self.total_urls == 0:
            return 0.0
        return (self.successful / self.total_urls) * 100
    
    @property
    def urls_per_second(self) -> float:
        """Calculate URLs processed per second"""
        if self.total_time == 0:
            return 0.0
        return self.total_urls / self.total_time
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization"""
        return {
            'method': self.method.value,
            'total_urls': self.total_urls,
            'successful': self.successful,
            'failed': self.failed,
            'success_rate': self.success_rate,
            'total_time': self.total_time,
            'average_response_time': self.average_response_time,
            'urls_per_second': self.urls_per_second,
            'content': [content.to_dict() for content in self.content],
            'errors': self.errors,
            'metadata': self.metadata
        }


@dataclass
class ScrapingConfig:
    """Configuration for scraping operations"""
    max_workers: int = 5
    rate_limit: float = 1.0  # seconds between requests
    timeout: int = 10
    retries: int = 3
    extract_title: bool = True
    extract_links: bool = True
    extract_text: bool = False
    max_text_length: int = 1000
    user_agent: str = "Web Scraper 1.0"
    
    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> 'ScrapingConfig':
        """Create config from dictionary"""
        concurrency = config_dict.get('concurrency', {})
        extraction = config_dict.get('extraction', {})
        
        return cls(
            max_workers=concurrency.get('max_workers', 5),
            rate_limit=concurrency.get('rate_limit', 1.0),
            timeout=concurrency.get('timeout', 10),
            retries=concurrency.get('retries', 3),
            extract_title=extraction.get('extract_title', True),
            extract_links=extraction.get('extract_links', True),
            extract_text=extraction.get('extract_text', False),
            max_text_length=extraction.get('max_text_length', 1000),
            user_agent=config_dict.get('user_agent', "Web Scraper 1.0")
        )


@dataclass
class PerformanceMetrics:
    """Performance metrics for comparison"""
    method: ScrapingMethod
    total_time: float
    urls_per_second: float
    success_rate: float
    average_response_time: float
    memory_usage_mb: float = 0.0
    cpu_usage_percent: float = 0.0
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization"""
        return {
            'method': self.method.value,
            'total_time': self.total_time,
            'urls_per_second': self.urls_per_second,
            'success_rate': self.success_rate,
            'average_response_time': self.average_response_time,
            'memory_usage_mb': self.memory_usage_mb,
            'cpu_usage_percent': self.cpu_usage_percent
        }