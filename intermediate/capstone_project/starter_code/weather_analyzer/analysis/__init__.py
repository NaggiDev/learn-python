"""
Analysis module for weather data processing and statistical analysis.

This module contains classes and functions for analyzing weather data,
calculating statistics, identifying trends, and generating insights.
"""

from .statistics import WeatherStatistics
from .trends import TrendAnalyzer

__all__ = ['WeatherStatistics', 'TrendAnalyzer']