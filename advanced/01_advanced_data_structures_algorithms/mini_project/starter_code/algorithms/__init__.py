"""
Algorithm Implementation Challenge Package

A comprehensive library of algorithms with performance analysis and testing.
This package includes implementations of sorting, searching, tree, and graph algorithms
with detailed complexity analysis and benchmarking capabilities.
"""

__version__ = "1.0.0"
__author__ = "Python Learning Path Student"

# Import main algorithm categories
from . import sorting
from . import searching
from . import trees
from . import graphs
from . import utils

__all__ = [
    "sorting",
    "searching", 
    "trees",
    "graphs",
    "utils",
]