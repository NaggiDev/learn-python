"""
Test cases for Text Processing Pipeline

This test file demonstrates testing text processing functionality
while reinforcing basic Python concepts.
"""

import os
import tempfile
import unittest
from solutions.text_processing_pipeline_solution import TextProcessor


class TestTextProcessor(unittest.TestCase):
    """Test cases for the TextProcessor class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.processor = TextProcessor()
        self.sample_text = "Hello world! This is a test. Python is great for text processing."
    
    def test_clean_text(self):
        """Test text cleaning functionality."""
        dirty_text = "  Hello,   WORLD!!!   This    is   a   TEST.  "
        cleaned = self.processor.clean_text(dirty_text)
        
        # Should be lowercase and normalized whitespace
        self.assertEqual(cleaned, "hello world! this is a test.")
    
    def test_extract_words(self):
        """Test word extraction."""
        text = "Hello, world! This is a test."
        words = self.processor.extract_words(text)
        
        expected_words = ["hello", "world", "this", "is", "a", "test"]
        self.assertEqual(words, expected_words)
    
    def test_extract_sentences(self):
        """Test sentence extraction."""
        text = "Hello world! This is a test. How are you?"
        sentences = self.processor.extract_sentences(text)
        
        expected_sentences = ["Hello world", "This is a test", "How are you"]
        self.assertEqual(sentences, expected_sentences)
    
    def test_process_text_basic(self):
        """Test basic text processing."""
        stats = self.processor.process_text(self.sample_text, "test")
        
        self.assertGreater(stats["word_count"], 0)
        self.assertGreater(stats["sentence_count"], 0)
        self.assertGreater(stats["char_count"], 0)
        self.assertGreater(stats["unique_words"], 0)
        self.assertGreater(stats["avg_word_length"], 0)
    
    def test_process_empty_text(self):
        """Test processing empty text."""
        stats = self.processor.process_text("", "empty")
        
        self.assertEqual(stats["word_count"], 0)
        self.assertEqual(stats["sentence_count"], 0)
        self.assertEqual(stats["char_count"], 0)
    
    def test_word_frequency_counting(self):
        """Test word frequency counting."""
        text = "the cat sat on the mat the cat was happy"
        self.processor.process_text(text, "test")
        
        # Check that frequencies are counted correctly
        self.assertEqual(self.processor.word_frequencies["the"], 3)
        self.assertEqual(self.processor.word_frequencies["cat"], 2)
        self.assertEqual(self.processor.word_frequencies["sat"], 1)
    
    def test_get_top_words(self):
        """Test getting top words."""
        text = "apple banana apple cherry apple banana"
        self.processor.process_text(text, "test")
        
        top_words = self.processor.get_top_words(3)
        
        # Should be sorted by frequency
        self.assertEqual(top_words[0][0], "apple")  # Most frequent
        self.assertEqual(top_words[0][1], 3)
        self.assertEqual(top_words[1][0], "banana")
        self.assertEqual(top_words[1][1], 2)
    
    def test_search_word_contexts(self):
        """Test word context search."""
        text = "The quick brown fox jumps over the lazy dog"
        self.processor.process_text(text, "test")
        
        contexts = self.processor.search_word_contexts("fox", 2)
        
        self.assertEqual(len(contexts), 1)
        self.assertIn("fox", contexts[0])
        self.assertIn("brown", contexts[0])
        self.assertIn("jumps", contexts[0])
    
    def test_filter_words_by_length(self):
        """Test filtering words by length."""
        text = "a big elephant runs quickly through the forest"
        self.processor.process_text(text, "test")
        
        # Filter words with length 5-8
        filtered = self.processor.filter_words_by_length(5, 8)
        
        # Should include "elephant" (8 chars) and "quickly" (7 chars)
        self.assertIn("elephant", filtered)
        self.assertIn("quickly", filtered)
        self.assertNotIn("a", filtered)  # Too short
        self.assertNotIn("big", filtered)  # Too short
    
    def test_reading_statistics(self):
        """Test reading statistics calculation."""
        # Process some text first
        text = "This is a sample text for testing reading statistics. " * 10
        self.processor.process_text(text, "test")
        
        stats = self.processor.get_reading_statistics()
        
        self.assertIn("total_words", stats)
        self.assertIn("estimated_reading_time_minutes", stats)
        self.assertIn("text_complexity", stats)
        self.assertGreater(stats["total_words"], 0)
        self.assertGreater(stats["estimated_reading_time_minutes"], 0)
    
    def test_generate_summary_report(self):
        """Test summary report generation."""
        # Process some text first
        self.processor.process_text(self.sample_text, "test")
        
        report = self.processor.generate_summary_report()
        
        self.assertIn("Summary Report", report)
        self.assertIn("Files processed", report)
        self.assertIn("Total words", report)
        self.assertIn("Top", report)
    
    def test_process_file_operations(self):
        """Test file processing operations."""
        # Create a temporary file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
            temp_file.write(self.sample_text)
            temp_file_path = temp_file.name
        
        try:
            # Test processing the file
            result = self.processor.process_file(temp_file_path)
            self.assertTrue(result)
            
            # Check that file was added to processed files
            self.assertIn(temp_file_path, self.processor.processed_files)
            
            # Check that content was processed
            filename = os.path.basename(temp_file_path)
            self.assertIn(filename, self.processor.file_stats)
            
        finally:
            # Clean up
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)
    
    def test_process_nonexistent_file(self):
        """Test processing a non-existent file."""
        result = self.processor.process_file("nonexistent_file.txt")
        self.assertFalse(result)
    
    def test_find_common_patterns(self):
        """Test finding common patterns."""
        text = "running runner runs quickly walking walker walks slowly"
        self.processor.process_text(text, "test")
        
        patterns = self.processor.find_common_patterns()
        
        self.assertIn("common_prefixes", patterns)
        self.assertIn("common_suffixes", patterns)
        self.assertIn("long_words", patterns)


def run_basic_functionality_tests():
    """Run basic functionality tests with simple assertions."""
    print("Running basic functionality tests...")
    
    processor = TextProcessor()
    
    # Test 1: Basic text processing
    text = "Hello world! This is a test. Python is great."
    stats = processor.process_text(text, "test1")
    
    assert stats["word_count"] > 0
    assert stats["sentence_count"] == 3
    assert stats["unique_words"] > 0
    
    # Test 2: Word frequency counting
    text2 = "apple banana apple cherry apple"
    processor.process_text(text2, "test2")
    
    top_words = processor.get_top_words(3)
    assert top_words[0][0] == "apple"
    assert top_words[0][1] == 3
    
    # Test 3: Text cleaning
    dirty_text = "  HELLO,   world!!!  "
    cleaned = processor.clean_text(dirty_text)
    assert "hello" in cleaned.lower()
    assert "world" in cleaned.lower()
    
    # Test 4: Word filtering
    text3 = "a big elephant runs quickly"
    processor.process_text(text3, "test3")
    
    long_words = processor.filter_words_by_length(5)
    assert "elephant" in long_words
    assert "quickly" in long_words
    assert "a" not in long_words
    
    # Test 5: Reading statistics
    reading_stats = processor.get_reading_statistics()
    assert "total_words" in reading_stats
    assert reading_stats["total_words"] > 0
    
    print("✓ All basic functionality tests passed!")


def create_sample_files_for_testing():
    """Create sample files for testing directory processing."""
    test_dir = "test_text_files"
    
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    
    sample_files = {
        "sample1.txt": "This is the first sample file. It contains some text for testing.",
        "sample2.txt": "This is the second sample file. It has different content than the first.",
        "sample3.md": "# Markdown File\n\nThis is a markdown file with some **bold** text.",
        "readme.txt": "This is a readme file. It explains how to use the text processor."
    }
    
    for filename, content in sample_files.items():
        filepath = os.path.join(test_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return test_dir


def cleanup_test_files(test_dir):
    """Clean up test files and directory."""
    if os.path.exists(test_dir):
        for filename in os.listdir(test_dir):
            filepath = os.path.join(test_dir, filename)
            if os.path.isfile(filepath):
                os.unlink(filepath)
        os.rmdir(test_dir)


def test_directory_processing():
    """Test directory processing functionality."""
    print("Testing directory processing...")
    
    # Create test files
    test_dir = create_sample_files_for_testing()
    
    try:
        processor = TextProcessor()
        
        # Process the directory
        count = processor.process_directory(test_dir)
        
        assert count > 0, "Should have processed some files"
        assert len(processor.processed_files) == count
        
        # Check that files were processed
        for filename in ["sample1.txt", "sample2.txt", "sample3.md", "readme.txt"]:
            assert filename in processor.file_stats
        
        # Generate report
        report = processor.generate_summary_report()
        assert "Files processed: 4" in report
        
        print(f"✓ Successfully processed {count} files from directory")
        
    finally:
        # Clean up
        cleanup_test_files(test_dir)


if __name__ == "__main__":
    print("Text Processing Pipeline - Test Suite")
    print("=" * 45)
    
    # Run basic functionality tests
    run_basic_functionality_tests()
    
    # Test directory processing
    test_directory_processing()
    
    print("\nRunning comprehensive unit tests...")
    unittest.main(verbosity=2)