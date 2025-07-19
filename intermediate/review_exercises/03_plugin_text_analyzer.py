"""
Plugin-Based Text Analyzer - Review Exercise

This exercise combines multiple intermediate concepts while introducing architectural patterns:
- Object-oriented programming (classes, inheritance, composition, abstract classes)
- Module organization and package structure
- Testing with mocks and fixtures
- Functional programming patterns (decorators, higher-order functions)
- Plugin architecture and dependency injection
- Introduction to software architecture patterns (advanced topic)

Requirements:
1. Create a TextAnalyzer system that can:
   - Load and manage plugins dynamically
   - Process text through multiple analysis plugins
   - Provide a plugin registry and discovery mechanism
   - Support plugin configuration and metadata
   - Implement plugin lifecycle management
   - Provide extensible analysis pipeline
   - Generate comprehensive analysis reports

2. Implement proper OOP design with abstract base classes and interfaces
3. Use decorators for plugin registration and configuration
4. Include comprehensive test coverage with plugin mocking
5. Demonstrate architectural patterns and design principles

This bridges to advanced concepts by introducing:
- Plugin architecture and extensibility patterns
- Dependency injection and inversion of control
- Software architecture design patterns
- Dynamic module loading and reflection
"""

import json
import re
import statistics
from abc import ABC, abstractmethod
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from functools import wraps
from typing import Any, Dict, List, Optional, Callable, Type, Set
import logging
import importlib
import inspect


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class PluginStatus(Enum):
    """Plugin status enumeration."""
    LOADED = "loaded"
    ACTIVE = "active"
    INACTIVE = "inactive"
    ERROR = "error"


class AnalysisType(Enum):
    """Types of text analysis."""
    STATISTICAL = "statistical"
    LINGUISTIC = "linguistic"
    SENTIMENT = "sentiment"
    STRUCTURAL = "structural"
    CUSTOM = "custom"


@dataclass
class PluginMetadata:
    """Metadata for text analysis plugins."""
    name: str
    version: str
    description: str
    author: str
    analysis_type: AnalysisType
    dependencies: List[str] = field(default_factory=list)
    config_schema: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)


@dataclass
class AnalysisResult:
    """Result of text analysis."""
    plugin_name: str
    analysis_type: AnalysisType
    data: Dict[str, Any]
    processing_time: float
    metadata: Dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass
class TextDocument:
    """Text document for analysis."""
    content: str
    title: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)


def plugin_decorator(name: str, version: str = "1.0.0", 
                    analysis_type: AnalysisType = AnalysisType.CUSTOM,
                    description: str = "", author: str = "Unknown") -> Callable:
    """
    Decorator to register a plugin class.
    
    Args:
        name: Plugin name
        version: Plugin version
        analysis_type: Type of analysis performed
        description: Plugin description
        author: Plugin author
        
    Returns:
        Decorator function
    """
    def decorator(cls):
        # TODO: Implement plugin registration decorator
        # - Add metadata to the class
        # - Register plugin in global registry
        # - Validate plugin interface
        cls._plugin_metadata = PluginMetadata(
            name=name,
            version=version,
            description=description,
            author=author,
            analysis_type=analysis_type
        )
        return cls
    return decorator


def config_decorator(config_schema: Dict[str, Any]) -> Callable:
    """
    Decorator to define plugin configuration schema.
    
    Args:
        config_schema: JSON schema for plugin configuration
        
    Returns:
        Decorator function
    """
    def decorator(cls):
        # TODO: Implement configuration decorator
        # - Add config schema to plugin metadata
        # - Validate configuration format
        if hasattr(cls, '_plugin_metadata'):
            cls._plugin_metadata.config_schema = config_schema
        return cls
    return decorator


def requires_dependencies(*dependencies: str) -> Callable:
    """
    Decorator to specify plugin dependencies.
    
    Args:
        dependencies: List of required dependencies
        
    Returns:
        Decorator function
    """
    def decorator(cls):
        # TODO: Implement dependencies decorator
        # - Add dependencies to plugin metadata
        # - Check dependency availability
        if hasattr(cls, '_plugin_metadata'):
            cls._plugin_metadata.dependencies = list(dependencies)
        return cls
    return decorator


class TextAnalysisPlugin(ABC):
    """Abstract base class for text analysis plugins."""
    
    def __init__(self, config: Dict[str, Any] = None):
        """
        Initialize plugin with configuration.
        
        Args:
            config: Plugin configuration dictionary
        """
        self.config = config or {}
        self.logger = logging.getLogger(f"plugin.{self.get_name()}")
        self.status = PluginStatus.LOADED
        self._initialize()
    
    @abstractmethod
    def analyze(self, document: TextDocument) -> AnalysisResult:
        """
        Analyze a text document.
        
        Args:
            document: Text document to analyze
            
        Returns:
            Analysis result
        """
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        """Get the plugin name."""
        pass
    
    @abstractmethod
    def get_analysis_type(self) -> AnalysisType:
        """Get the type of analysis performed by this plugin."""
        pass
    
    def _initialize(self) -> None:
        """Initialize plugin-specific resources."""
        # TODO: Implement plugin initialization
        # - Validate configuration
        # - Set up resources
        # - Update status
        pass
    
    def validate_config(self, config: Dict[str, Any]) -> bool:
        """
        Validate plugin configuration.
        
        Args:
            config: Configuration to validate
            
        Returns:
            True if configuration is valid
        """
        # TODO: Implement configuration validation
        # - Check against config schema
        # - Validate required fields
        # - Check data types
        return True
    
    def get_metadata(self) -> PluginMetadata:
        """Get plugin metadata."""
        # TODO: Implement metadata retrieval
        if hasattr(self.__class__, '_plugin_metadata'):
            return self.__class__._plugin_metadata
        return PluginMetadata(
            name=self.get_name(),
            version="1.0.0",
            description="No description available",
            author="Unknown",
            analysis_type=self.get_analysis_type()
        )
    
    def get_status(self) -> PluginStatus:
        """Get current plugin status."""
        return self.status
    
    def activate(self) -> None:
        """Activate the plugin."""
        # TODO: Implement plugin activation
        self.status = PluginStatus.ACTIVE
    
    def deactivate(self) -> None:
        """Deactivate the plugin."""
        # TODO: Implement plugin deactivation
        self.status = PluginStatus.INACTIVE
    
    def cleanup(self) -> None:
        """Clean up plugin resources."""
        # TODO: Implement resource cleanup
        pass


@plugin_decorator("word_count", "1.0.0", AnalysisType.STATISTICAL, 
                 "Counts words, characters, and sentences", "TextAnalyzer Team")
class WordCountPlugin(TextAnalysisPlugin):
    """Plugin for basic word and character counting."""
    
    def analyze(self, document: TextDocument) -> AnalysisResult:
        """Analyze word count statistics."""
        # TODO: Implement word count analysis
        # - Count words, characters, sentences, paragraphs
        # - Calculate averages
        # - Return structured results
        import time
        start_time = time.time()
        
        text = document.content
        
        # Basic counts
        word_count = len(text.split())
        char_count = len(text)
        char_count_no_spaces = len(text.replace(' ', ''))
        sentence_count = len([s for s in re.split(r'[.!?]+', text) if s.strip()])
        paragraph_count = len([p for p in text.split('\n\n') if p.strip()])
        
        # Averages
        avg_words_per_sentence = word_count / max(sentence_count, 1)
        avg_chars_per_word = char_count_no_spaces / max(word_count, 1)
        
        processing_time = time.time() - start_time
        
        return AnalysisResult(
            plugin_name=self.get_name(),
            analysis_type=self.get_analysis_type(),
            data={
                "word_count": word_count,
                "character_count": char_count,
                "character_count_no_spaces": char_count_no_spaces,
                "sentence_count": sentence_count,
                "paragraph_count": paragraph_count,
                "average_words_per_sentence": round(avg_words_per_sentence, 2),
                "average_characters_per_word": round(avg_chars_per_word, 2)
            },
            processing_time=processing_time
        )
    
    def get_name(self) -> str:
        return "word_count"
    
    def get_analysis_type(self) -> AnalysisType:
        return AnalysisType.STATISTICAL


@plugin_decorator("readability", "1.0.0", AnalysisType.LINGUISTIC,
                 "Calculates readability scores", "TextAnalyzer Team")
@config_decorator({
    "include_flesch_kincaid": {"type": "boolean", "default": True},
    "include_gunning_fog": {"type": "boolean", "default": True}
})
class ReadabilityPlugin(TextAnalysisPlugin):
    """Plugin for readability analysis."""
    
    def analyze(self, document: TextDocument) -> AnalysisResult:
        """Analyze text readability."""
        # TODO: Implement readability analysis
        # - Calculate Flesch Reading Ease
        # - Calculate Flesch-Kincaid Grade Level
        # - Calculate Gunning Fog Index
        # - Return readability scores
        import time
        start_time = time.time()
        
        text = document.content
        
        # Basic metrics for readability calculations
        sentences = [s for s in re.split(r'[.!?]+', text) if s.strip()]
        words = text.split()
        syllables = sum(self._count_syllables(word) for word in words)
        
        sentence_count = len(sentences)
        word_count = len(words)
        syllable_count = syllables
        
        # Avoid division by zero
        if sentence_count == 0 or word_count == 0:
            processing_time = time.time() - start_time
            return AnalysisResult(
                plugin_name=self.get_name(),
                analysis_type=self.get_analysis_type(),
                data={"error": "Insufficient text for readability analysis"},
                processing_time=processing_time
            )
        
        # Flesch Reading Ease
        flesch_ease = 206.835 - (1.015 * (word_count / sentence_count)) - (84.6 * (syllable_count / word_count))
        
        # Flesch-Kincaid Grade Level
        flesch_kincaid = (0.39 * (word_count / sentence_count)) + (11.8 * (syllable_count / word_count)) - 15.59
        
        # Gunning Fog Index (simplified)
        complex_words = sum(1 for word in words if self._count_syllables(word) >= 3)
        gunning_fog = 0.4 * ((word_count / sentence_count) + (100 * (complex_words / word_count)))
        
        processing_time = time.time() - start_time
        
        return AnalysisResult(
            plugin_name=self.get_name(),
            analysis_type=self.get_analysis_type(),
            data={
                "flesch_reading_ease": round(flesch_ease, 2),
                "flesch_kincaid_grade": round(flesch_kincaid, 2),
                "gunning_fog_index": round(gunning_fog, 2),
                "readability_level": self._get_readability_level(flesch_ease),
                "metrics": {
                    "sentence_count": sentence_count,
                    "word_count": word_count,
                    "syllable_count": syllable_count,
                    "complex_words": complex_words
                }
            },
            processing_time=processing_time
        )
    
    def _count_syllables(self, word: str) -> int:
        """Count syllables in a word (simplified algorithm)."""
        word = word.lower()
        vowels = "aeiouy"
        syllable_count = 0
        previous_was_vowel = False
        
        for char in word:
            is_vowel = char in vowels
            if is_vowel and not previous_was_vowel:
                syllable_count += 1
            previous_was_vowel = is_vowel
        
        # Handle silent 'e'
        if word.endswith('e') and syllable_count > 1:
            syllable_count -= 1
        
        return max(syllable_count, 1)
    
    def _get_readability_level(self, flesch_score: float) -> str:
        """Get readability level description from Flesch score."""
        if flesch_score >= 90:
            return "Very Easy"
        elif flesch_score >= 80:
            return "Easy"
        elif flesch_score >= 70:
            return "Fairly Easy"
        elif flesch_score >= 60:
            return "Standard"
        elif flesch_score >= 50:
            return "Fairly Difficult"
        elif flesch_score >= 30:
            return "Difficult"
        else:
            return "Very Difficult"
    
    def get_name(self) -> str:
        return "readability"
    
    def get_analysis_type(self) -> AnalysisType:
        return AnalysisType.LINGUISTIC


@plugin_decorator("keyword_frequency", "1.0.0", AnalysisType.STATISTICAL,
                 "Analyzes keyword frequency and distribution", "TextAnalyzer Team")
@config_decorator({
    "min_word_length": {"type": "integer", "default": 3},
    "max_keywords": {"type": "integer", "default": 20},
    "exclude_stopwords": {"type": "boolean", "default": True}
})
class KeywordFrequencyPlugin(TextAnalysisPlugin):
    """Plugin for keyword frequency analysis."""
    
    def __init__(self, config: Dict[str, Any] = None):
        super().__init__(config)
        self.stopwords = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with',
            'by', 'from', 'up', 'about', 'into', 'through', 'during', 'before', 'after',
            'above', 'below', 'between', 'among', 'is', 'are', 'was', 'were', 'be', 'been',
            'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
            'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these', 'those'
        }
    
    def analyze(self, document: TextDocument) -> AnalysisResult:
        """Analyze keyword frequency."""
        # TODO: Implement keyword frequency analysis
        # - Extract and clean words
        # - Filter by length and stopwords
        # - Calculate frequencies
        # - Return top keywords
        import time
        start_time = time.time()
        
        text = document.content.lower()
        
        # Extract words and clean them
        words = re.findall(r'\b[a-zA-Z]+\b', text)
        
        # Apply filters
        min_length = self.config.get('min_word_length', 3)
        exclude_stopwords = self.config.get('exclude_stopwords', True)
        max_keywords = self.config.get('max_keywords', 20)
        
        filtered_words = []
        for word in words:
            if len(word) >= min_length:
                if not exclude_stopwords or word not in self.stopwords:
                    filtered_words.append(word)
        
        # Calculate frequencies
        word_freq = Counter(filtered_words)
        total_words = len(filtered_words)
        
        # Get top keywords
        top_keywords = word_freq.most_common(max_keywords)
        
        # Calculate statistics
        unique_words = len(word_freq)
        vocabulary_richness = unique_words / max(total_words, 1)
        
        processing_time = time.time() - start_time
        
        return AnalysisResult(
            plugin_name=self.get_name(),
            analysis_type=self.get_analysis_type(),
            data={
                "top_keywords": [{"word": word, "count": count, "frequency": count/total_words} 
                               for word, count in top_keywords],
                "total_words_analyzed": total_words,
                "unique_words": unique_words,
                "vocabulary_richness": round(vocabulary_richness, 4),
                "most_frequent_word": top_keywords[0] if top_keywords else None,
                "config_used": {
                    "min_word_length": min_length,
                    "exclude_stopwords": exclude_stopwords,
                    "max_keywords": max_keywords
                }
            },
            processing_time=processing_time
        )
    
    def get_name(self) -> str:
        return "keyword_frequency"
    
    def get_analysis_type(self) -> AnalysisType:
        return AnalysisType.STATISTICAL


class PluginRegistry:
    """Registry for managing text analysis plugins."""
    
    def __init__(self):
        """Initialize plugin registry."""
        self.plugins: Dict[str, Type[TextAnalysisPlugin]] = {}
        self.instances: Dict[str, TextAnalysisPlugin] = {}
        self.logger = logging.getLogger("plugin_registry")
    
    def register_plugin(self, plugin_class: Type[TextAnalysisPlugin]) -> None:
        """
        Register a plugin class.
        
        Args:
            plugin_class: Plugin class to register
        """
        # TODO: Implement plugin registration
        # - Validate plugin interface
        # - Check for name conflicts
        # - Store plugin class
        if not issubclass(plugin_class, TextAnalysisPlugin):
            raise ValueError(f"Plugin {plugin_class} must inherit from TextAnalysisPlugin")
        
        # Get plugin name from metadata or class
        if hasattr(plugin_class, '_plugin_metadata'):
            plugin_name = plugin_class._plugin_metadata.name
        else:
            # Fallback to creating instance to get name
            temp_instance = plugin_class()
            plugin_name = temp_instance.get_name()
        
        if plugin_name in self.plugins:
            self.logger.warning(f"Plugin {plugin_name} already registered, overwriting")
        
        self.plugins[plugin_name] = plugin_class
        self.logger.info(f"Registered plugin: {plugin_name}")
    
    def unregister_plugin(self, plugin_name: str) -> None:
        """
        Unregister a plugin.
        
        Args:
            plugin_name: Name of plugin to unregister
        """
        # TODO: Implement plugin unregistration
        if plugin_name in self.plugins:
            # Clean up instance if exists
            if plugin_name in self.instances:
                self.instances[plugin_name].cleanup()
                del self.instances[plugin_name]
            
            del self.plugins[plugin_name]
            self.logger.info(f"Unregistered plugin: {plugin_name}")
        else:
            self.logger.warning(f"Plugin {plugin_name} not found for unregistration")
    
    def get_plugin(self, plugin_name: str, config: Dict[str, Any] = None) -> TextAnalysisPlugin:
        """
        Get a plugin instance.
        
        Args:
            plugin_name: Name of the plugin
            config: Plugin configuration
            
        Returns:
            Plugin instance
        """
        # TODO: Implement plugin instance retrieval
        if plugin_name not in self.plugins:
            raise ValueError(f"Plugin {plugin_name} not registered")
        
        # Create new instance or return existing one
        if plugin_name not in self.instances:
            plugin_class = self.plugins[plugin_name]
            self.instances[plugin_name] = plugin_class(config)
        
        return self.instances[plugin_name]
    
    def list_plugins(self) -> List[str]:
        """Get list of registered plugin names."""
        return list(self.plugins.keys())
    
    def get_plugin_metadata(self, plugin_name: str) -> PluginMetadata:
        """
        Get metadata for a plugin.
        
        Args:
            plugin_name: Name of the plugin
            
        Returns:
            Plugin metadata
        """
        # TODO: Implement metadata retrieval
        if plugin_name not in self.plugins:
            raise ValueError(f"Plugin {plugin_name} not registered")
        
        plugin_class = self.plugins[plugin_name]
        if hasattr(plugin_class, '_plugin_metadata'):
            return plugin_class._plugin_metadata
        
        # Fallback to creating instance
        temp_instance = plugin_class()
        return temp_instance.get_metadata()
    
    def get_plugins_by_type(self, analysis_type: AnalysisType) -> List[str]:
        """
        Get plugins by analysis type.
        
        Args:
            analysis_type: Type of analysis
            
        Returns:
            List of plugin names
        """
        # TODO: Implement filtering by analysis type
        matching_plugins = []
        for plugin_name in self.plugins:
            metadata = self.get_plugin_metadata(plugin_name)
            if metadata.analysis_type == analysis_type:
                matching_plugins.append(plugin_name)
        return matching_plugins
    
    def validate_dependencies(self, plugin_name: str) -> bool:
        """
        Validate plugin dependencies.
        
        Args:
            plugin_name: Name of the plugin
            
        Returns:
            True if all dependencies are satisfied
        """
        # TODO: Implement dependency validation
        metadata = self.get_plugin_metadata(plugin_name)
        for dependency in metadata.dependencies:
            if dependency not in self.plugins:
                self.logger.error(f"Plugin {plugin_name} requires {dependency} which is not registered")
                return False
        return True


class AnalysisPipeline:
    """Pipeline for running multiple analysis plugins."""
    
    def __init__(self, registry: PluginRegistry):
        """
        Initialize analysis pipeline.
        
        Args:
            registry: Plugin registry
        """
        self.registry = registry
        self.pipeline_plugins: List[str] = []
        self.plugin_configs: Dict[str, Dict[str, Any]] = {}
        self.logger = logging.getLogger("analysis_pipeline")
    
    def add_plugin(self, plugin_name: str, config: Dict[str, Any] = None) -> None:
        """
        Add a plugin to the pipeline.
        
        Args:
            plugin_name: Name of the plugin
            config: Plugin configuration
        """
        # TODO: Implement plugin addition to pipeline
        if plugin_name not in self.registry.list_plugins():
            raise ValueError(f"Plugin {plugin_name} not registered")
        
        if not self.registry.validate_dependencies(plugin_name):
            raise ValueError(f"Plugin {plugin_name} has unmet dependencies")
        
        self.pipeline_plugins.append(plugin_name)
        if config:
            self.plugin_configs[plugin_name] = config
        
        self.logger.info(f"Added plugin {plugin_name} to pipeline")
    
    def remove_plugin(self, plugin_name: str) -> None:
        """
        Remove a plugin from the pipeline.
        
        Args:
            plugin_name: Name of the plugin to remove
        """
        # TODO: Implement plugin removal from pipeline
        if plugin_name in self.pipeline_plugins:
            self.pipeline_plugins.remove(plugin_name)
            if plugin_name in self.plugin_configs:
                del self.plugin_configs[plugin_name]
            self.logger.info(f"Removed plugin {plugin_name} from pipeline")
    
    def analyze_document(self, document: TextDocument) -> Dict[str, AnalysisResult]:
        """
        Analyze a document using all plugins in the pipeline.
        
        Args:
            document: Document to analyze
            
        Returns:
            Dictionary mapping plugin names to analysis results
        """
        # TODO: Implement document analysis through pipeline
        results = {}
        
        for plugin_name in self.pipeline_plugins:
            try:
                config = self.plugin_configs.get(plugin_name, {})
                plugin = self.registry.get_plugin(plugin_name, config)
                
                if plugin.get_status() != PluginStatus.ACTIVE:
                    plugin.activate()
                
                result = plugin.analyze(document)
                results[plugin_name] = result
                
                self.logger.info(f"Plugin {plugin_name} completed analysis in {result.processing_time:.3f}s")
                
            except Exception as e:
                self.logger.error(f"Plugin {plugin_name} failed: {str(e)}")
                results[plugin_name] = AnalysisResult(
                    plugin_name=plugin_name,
                    analysis_type=AnalysisType.CUSTOM,
                    data={"error": str(e)},
                    processing_time=0.0
                )
        
        return results
    
    def get_pipeline_info(self) -> Dict[str, Any]:
        """Get information about the current pipeline."""
        # TODO: Implement pipeline information retrieval
        return {
            "plugins": self.pipeline_plugins,
            "plugin_count": len(self.pipeline_plugins),
            "configurations": self.plugin_configs,
            "analysis_types": [
                self.registry.get_plugin_metadata(name).analysis_type.value 
                for name in self.pipeline_plugins
            ]
        }


class TextAnalyzer:
    """Main text analyzer class that orchestrates the analysis process."""
    
    def __init__(self):
        """Initialize text analyzer."""
        self.registry = PluginRegistry()
        self.pipeline = AnalysisPipeline(self.registry)
        self.logger = logging.getLogger("text_analyzer")
        
        # Register built-in plugins
        self._register_builtin_plugins()
    
    def _register_builtin_plugins(self) -> None:
        """Register built-in plugins."""
        # TODO: Implement built-in plugin registration
        builtin_plugins = [
            WordCountPlugin,
            ReadabilityPlugin,
            KeywordFrequencyPlugin
        ]
        
        for plugin_class in builtin_plugins:
            self.registry.register_plugin(plugin_class)
    
    def analyze_text(self, text: str, title: str = "", 
                    plugins: List[str] = None) -> Dict[str, AnalysisResult]:
        """
        Analyze text using specified plugins.
        
        Args:
            text: Text to analyze
            title: Optional title for the document
            plugins: List of plugin names to use (default: all registered)
            
        Returns:
            Dictionary mapping plugin names to analysis results
        """
        # TODO: Implement text analysis
        document = TextDocument(content=text, title=title)
        
        # Set up pipeline with specified plugins
        if plugins is None:
            plugins = self.registry.list_plugins()
        
        # Clear current pipeline and add specified plugins
        self.pipeline.pipeline_plugins.clear()
        for plugin_name in plugins:
            self.pipeline.add_plugin(plugin_name)
        
        return self.pipeline.analyze_document(document)
    
    def generate_report(self, results: Dict[str, AnalysisResult], 
                       format_type: str = "text") -> str:
        """
        Generate a formatted analysis report.
        
        Args:
            results: Analysis results from plugins
            format_type: Report format ("text", "json", "html")
            
        Returns:
            Formatted report string
        """
        # TODO: Implement report generation
        if format_type == "json":
            return self._generate_json_report(results)
        elif format_type == "html":
            return self._generate_html_report(results)
        else:
            return self._generate_text_report(results)
    
    def _generate_text_report(self, results: Dict[str, AnalysisResult]) -> str:
        """Generate a text-based report."""
        # TODO: Implement text report generation
        report_lines = []
        report_lines.append("=" * 60)
        report_lines.append("TEXT ANALYSIS REPORT")
        report_lines.append("=" * 60)
        report_lines.append(f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append(f"Plugins used: {len(results)}")
        report_lines.append("")
        
        for plugin_name, result in results.items():
            report_lines.append(f"--- {plugin_name.upper()} ANALYSIS ---")
            report_lines.append(f"Processing time: {result.processing_time:.3f} seconds")
            report_lines.append(f"Analysis type: {result.analysis_type.value}")
            
            if "error" in result.data:
                report_lines.append(f"Error: {result.data['error']}")
            else:
                for key, value in result.data.items():
                    if isinstance(value, dict):
                        report_lines.append(f"{key}:")
                        for sub_key, sub_value in value.items():
                            report_lines.append(f"  {sub_key}: {sub_value}")
                    elif isinstance(value, list):
                        report_lines.append(f"{key}: {len(value)} items")
                        for i, item in enumerate(value[:5]):  # Show first 5 items
                            report_lines.append(f"  {i+1}. {item}")
                        if len(value) > 5:
                            report_lines.append(f"  ... and {len(value) - 5} more")
                    else:
                        report_lines.append(f"{key}: {value}")
            
            report_lines.append("")
        
        return "\n".join(report_lines)
    
    def _generate_json_report(self, results: Dict[str, AnalysisResult]) -> str:
        """Generate a JSON report."""
        # TODO: Implement JSON report generation
        report_data = {
            "timestamp": datetime.now().isoformat(),
            "plugins_used": len(results),
            "results": {}
        }
        
        for plugin_name, result in results.items():
            report_data["results"][plugin_name] = {
                "analysis_type": result.analysis_type.value,
                "processing_time": result.processing_time,
                "data": result.data,
                "metadata": result.metadata
            }
        
        return json.dumps(report_data, indent=2)
    
    def _generate_html_report(self, results: Dict[str, AnalysisResult]) -> str:
        """Generate an HTML report."""
        # TODO: Implement HTML report generation
        html_parts = [
            "<!DOCTYPE html>",
            "<html><head><title>Text Analysis Report</title>",
            "<style>body{font-family:Arial,sans-serif;margin:20px;}",
            ".plugin{border:1px solid #ccc;margin:10px 0;padding:15px;}",
            ".plugin h3{margin-top:0;color:#333;}",
            ".data{background:#f5f5f5;padding:10px;margin:10px 0;}",
            "</style></head><body>",
            "<h1>Text Analysis Report</h1>",
            f"<p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>",
            f"<p>Plugins used: {len(results)}</p>"
        ]
        
        for plugin_name, result in results.items():
            html_parts.extend([
                f'<div class="plugin">',
                f'<h3>{plugin_name.title()} Analysis</h3>',
                f'<p>Processing time: {result.processing_time:.3f} seconds</p>',
                f'<p>Analysis type: {result.analysis_type.value}</p>',
                '<div class="data">'
            ])
            
            if "error" in result.data:
                html_parts.append(f'<p><strong>Error:</strong> {result.data["error"]}</p>')
            else:
                for key, value in result.data.items():
                    html_parts.append(f'<p><strong>{key}:</strong> {value}</p>')
            
            html_parts.extend(['</div>', '</div>'])
        
        html_parts.extend(['</body></html>'])
        return '\n'.join(html_parts)
    
    def get_available_plugins(self) -> List[Dict[str, Any]]:
        """Get information about available plugins."""
        # TODO: Implement available plugins listing
        plugins_info = []
        for plugin_name in self.registry.list_plugins():
            metadata = self.registry.get_plugin_metadata(plugin_name)
            plugins_info.append({
                "name": metadata.name,
                "version": metadata.version,
                "description": metadata.description,
                "author": metadata.author,
                "analysis_type": metadata.analysis_type.value,
                "dependencies": metadata.dependencies
            })
        return plugins_info


def demonstrate_plugin_system():
    """Demonstrate the plugin-based text analyzer."""
    print("Plugin-Based Text Analyzer Demonstration")
    print("=" * 50)
    
    # Create analyzer
    analyzer = TextAnalyzer()
    
    # Sample text for analysis
    sample_text = """
    The quick brown fox jumps over the lazy dog. This is a sample text for demonstrating
    the plugin-based text analysis system. The system can analyze various aspects of text
    including word count, readability, and keyword frequency. Each plugin provides specific
    analysis capabilities that can be combined to create comprehensive text analysis reports.
    
    This text contains multiple sentences and paragraphs to provide meaningful analysis results.
    The readability analysis will calculate scores based on sentence length and word complexity.
    The keyword frequency analysis will identify the most common words and their distribution.
    """
    
    print("Sample text loaded for analysis")
    print(f"Text length: {len(sample_text)} characters")
    
    # Show available plugins
    print("\nAvailable plugins:")
    for plugin_info in analyzer.get_available_plugins():
        print(f"- {plugin_info['name']} v{plugin_info['version']}: {plugin_info['description']}")
    
    # Analyze text
    print("\nRunning analysis...")
    results = analyzer.analyze_text(sample_text, "Sample Text Analysis")
    
    # Generate and display report
    print("\n" + "="*60)
    print("ANALYSIS RESULTS")
    print("="*60)
    
    text_report = analyzer.generate_report(results, "text")
    print(text_report)
    
    # Show JSON format
    print("\n" + "="*60)
    print("JSON FORMAT SAMPLE")
    print("="*60)
    json_report = analyzer.generate_report(results, "json")
    print(json_report[:500] + "..." if len(json_report) > 500 else json_report)


def main():
    """Main function with menu-driven interface."""
    print("=== Plugin-Based Text Analyzer ===")
    print("1. Run demonstration")
    print("2. Analyze custom text")
    print("3. Show available plugins")
    print("4. Test individual plugins")
    print("5. Exit")
    
    analyzer = TextAnalyzer()
    
    while True:
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            demonstrate_plugin_system()
            
        elif choice == "2":
            # TODO: Implement custom text analysis
            print("Enter text to analyze (press Enter twice to finish):")
            lines = []
            while True:
                line = input()
                if line == "" and lines and lines[-1] == "":
                    break
                lines.append(line)
            
            text = "\n".join(lines[:-1])  # Remove last empty line
            if text.strip():
                results = analyzer.analyze_text(text, "Custom Text")
                report = analyzer.generate_report(results, "text")
                print(report)
            else:
                print("No text provided.")
            
        elif choice == "3":
            print("\nAvailable plugins:")
            for plugin_info in analyzer.get_available_plugins():
                print(f"- {plugin_info['name']} v{plugin_info['version']}")
                print(f"  Description: {plugin_info['description']}")
                print(f"  Type: {plugin_info['analysis_type']}")
                print(f"  Author: {plugin_info['author']}")
                if plugin_info['dependencies']:
                    print(f"  Dependencies: {', '.join(plugin_info['dependencies'])}")
                print()
            
        elif choice == "4":
            # TODO: Implement individual plugin testing
            print("Individual plugin testing not yet implemented")
            
        elif choice == "5":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()