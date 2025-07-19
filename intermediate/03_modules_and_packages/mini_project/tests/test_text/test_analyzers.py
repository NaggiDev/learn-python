"""Tests for text analysis utilities."""

import pytest
from devtools.text.analyzers import word_count, analyze_readability, count_characters
from devtools.exceptions import ProcessingError

class TestWordCount:
    """Test word_count function."""
    
    def test_simple_text(self):
        """Test word count with simple text."""
        assert word_count("hello world") == 2
    
    def test_empty_string(self):
        """Test word count with empty string."""
        assert word_count("") == 0
    
    def test_whitespace_only(self):
        """Test word count with whitespace only."""
        assert word_count("   ") == 0
    
    def test_multiple_spaces(self):
        """Test word count with multiple spaces."""
        assert word_count("hello    world") == 2
    
    def test_single_word(self):
        """Test word count with single word."""
        assert word_count("hello") == 1
    
    def test_invalid_input(self):
        """Test word count with invalid input."""
        with pytest.raises(ProcessingError):
            word_count(123)
    
    def test_punctuation(self):
        """Test word count with punctuation."""
        assert word_count("Hello, world!") == 2

class TestCountCharacters:
    """Test count_characters function."""
    
    def test_simple_text(self):
        """Test character count with simple text."""
        assert count_characters("hello") == 5
    
    def test_with_spaces(self):
        """Test character count including spaces."""
        assert count_characters("hello world", include_spaces=True) == 11
    
    def test_without_spaces(self):
        """Test character count excluding spaces."""
        assert count_characters("hello world", include_spaces=False) == 10
    
    def test_empty_string(self):
        """Test character count with empty string."""
        assert count_characters("") == 0
    
    def test_invalid_input(self):
        """Test character count with invalid input."""
        with pytest.raises(ProcessingError):
            count_characters(123)

class TestAnalyzeReadability:
    """Test analyze_readability function."""
    
    def test_simple_sentence(self):
        """Test readability analysis with simple sentence."""
        result = analyze_readability("This is a test.")
        assert result['sentence_count'] == 1
        assert result['word_count'] == 4
        assert result['avg_sentence_length'] == 4.0
    
    def test_multiple_sentences(self):
        """Test readability analysis with multiple sentences."""
        text = "This is a test. This is another test!"
        result = analyze_readability(text)
        assert result['sentence_count'] == 2
        assert result['word_count'] == 8
        assert result['avg_sentence_length'] == 4.0
    
    def test_empty_text(self):
        """Test readability analysis with empty text."""
        result = analyze_readability("")
        assert result['sentence_count'] == 0
        assert result['word_count'] == 0
        assert result['avg_sentence_length'] == 0.0
    
    def test_invalid_input(self):
        """Test readability analysis with invalid input."""
        with pytest.raises(ProcessingError):
            analyze_readability(123)
    
    def test_complex_text(self):
        """Test readability analysis with complex text."""
        text = "Hello world! How are you? I am fine, thank you."
        result = analyze_readability(text)
        assert result['sentence_count'] == 3
        assert result['word_count'] == 10
        assert 'avg_word_length' in result
        assert 'character_count' in result