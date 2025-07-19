"""
Text Processing Pipeline - Review Exercise

This exercise combines multiple basic concepts:
- String manipulation and processing
- File operations (reading multiple files)
- Lists and dictionaries for data aggregation
- Functions and modular programming
- Control flow and error handling

Requirements:
1. Create a TextProcessor class that can:
   - Read and process multiple text files
   - Count word frequencies across all files
   - Analyze text statistics (word count, sentence count, etc.)
   - Generate summary reports
   - Filter and search text content

2. Implement text cleaning and normalization
3. Handle different file encodings and errors gracefully
4. Provide both file-based and string-based processing

This bridges to intermediate concepts by introducing:
- Data processing pipelines
- Text analysis patterns
- Functional programming concepts (map, filter operations)
- Statistical analysis basics
"""

import os
import re
import string
from collections import defaultdict
from typing import Dict, List, Tuple, Set, Optional


class TextProcessor:
    """A text processing pipeline that combines basic Python concepts."""
    
    def __init__(self):
        """Initialize the text processor."""
        self.word_frequencies = defaultdict(int)
        self.file_stats = {}  # filename -> stats dict
        self.processed_files = []
        
    def clean_text(self, text: str) -> str:
        """
        Clean and normalize text for processing.
        
        Args:
            text: Raw text to clean
            
        Returns:
            Cleaned text
        """
        # TODO: Implement text cleaning
        # - Convert to lowercase
        # - Remove extra whitespace
        # - Handle punctuation appropriately
        # - Remove or handle special characters
        pass
    
    def extract_words(self, text: str) -> List[str]:
        """
        Extract words from cleaned text.
        
        Args:
            text: Cleaned text
            
        Returns:
            List of words
        """
        # TODO: Implement word extraction
        # - Split text into words
        # - Filter out empty strings
        # - Handle punctuation and special cases
        pass
    
    def extract_sentences(self, text: str) -> List[str]:
        """
        Extract sentences from text.
        
        Args:
            text: Text to process
            
        Returns:
            List of sentences
        """
        # TODO: Implement sentence extraction
        # - Split text into sentences
        # - Handle different sentence endings (., !, ?)
        # - Clean up sentence boundaries
        pass
    
    def process_text(self, text: str, source_name: str = "string_input") -> Dict:
        """
        Process a single text and update statistics.
        
        Args:
            text: Text to process
            source_name: Name/identifier for the text source
            
        Returns:
            Dictionary with processing statistics
        """
        # TODO: Implement text processing
        # - Clean the text
        # - Extract words and sentences
        # - Update word frequencies
        # - Calculate statistics (word count, sentence count, etc.)
        # - Store results in file_stats
        # - Return statistics dictionary
        pass
    
    def process_file(self, filepath: str) -> bool:
        """
        Process a single text file.
        
        Args:
            filepath: Path to the text file
            
        Returns:
            True if successful, False otherwise
        """
        # TODO: Implement file processing
        # - Read file with proper encoding handling
        # - Process the text content
        # - Handle file reading errors
        # - Add to processed_files list
        # - Return success status
        pass
    
    def process_directory(self, directory_path: str, file_extensions: List[str] = None) -> int:
        """
        Process all text files in a directory.
        
        Args:
            directory_path: Path to directory
            file_extensions: List of extensions to process (default: ['.txt', '.md'])
            
        Returns:
            Number of files successfully processed
        """
        # TODO: Implement directory processing
        # - Get list of files with specified extensions
        # - Process each file
        # - Count successful processing
        # - Handle directory access errors
        pass
    
    def get_top_words(self, n: int = 10) -> List[Tuple[str, int]]:
        """
        Get the top N most frequent words.
        
        Args:
            n: Number of top words to return
            
        Returns:
            List of (word, frequency) tuples, sorted by frequency
        """
        # TODO: Implement top words extraction
        # - Sort word frequencies
        # - Return top N words with their counts
        pass
    
    def search_word_contexts(self, word: str, context_size: int = 5) -> List[str]:
        """
        Find contexts where a specific word appears.
        
        Args:
            word: Word to search for
            context_size: Number of words before and after to include
            
        Returns:
            List of context strings
        """
        # TODO: Implement word context search
        # - Search through processed files
        # - Extract context around the target word
        # - Return list of context strings
        pass
    
    def generate_summary_report(self) -> str:
        """
        Generate a comprehensive summary report.
        
        Returns:
            Formatted summary report
        """
        # TODO: Implement summary report generation
        # - Include overall statistics
        # - Show top words
        # - Include per-file statistics
        # - Format nicely with proper alignment
        pass
    
    def get_reading_statistics(self) -> Dict:
        """
        Calculate reading-related statistics.
        
        Returns:
            Dictionary with reading statistics
        """
        # TODO: Implement reading statistics
        # - Calculate average words per sentence
        # - Estimate reading time (assume 200 words per minute)
        # - Calculate text complexity metrics
        # - Return statistics dictionary
        pass
    
    def filter_words_by_length(self, min_length: int, max_length: int = None) -> Dict[str, int]:
        """
        Filter words by length and return their frequencies.
        
        Args:
            min_length: Minimum word length
            max_length: Maximum word length (optional)
            
        Returns:
            Dictionary of filtered words and their frequencies
        """
        # TODO: Implement word filtering by length
        # - Filter word_frequencies by length criteria
        # - Return filtered dictionary
        pass
    
    def find_common_patterns(self) -> Dict[str, List[str]]:
        """
        Find common patterns in the text (prefixes, suffixes, etc.).
        
        Returns:
            Dictionary mapping pattern types to lists of patterns
        """
        # TODO: Implement pattern finding
        # - Find common prefixes and suffixes
        # - Identify repeated phrases
        # - Find words with similar patterns
        # - Return organized results
        pass


def demonstrate_text_processing():
    """Demonstrate the text processing capabilities."""
    processor = TextProcessor()
    
    # Sample texts for demonstration
    sample_texts = [
        "The quick brown fox jumps over the lazy dog. This is a sample sentence for testing.",
        "Python is a powerful programming language. It is used for web development, data analysis, and more.",
        "Text processing is an important skill in programming. Regular expressions are very useful for this task."
    ]
    
    print("Text Processing Pipeline Demonstration")
    print("=" * 50)
    
    # Process sample texts
    for i, text in enumerate(sample_texts, 1):
        print(f"\nProcessing sample text {i}...")
        stats = processor.process_text(text, f"sample_{i}")
        print(f"Words: {stats.get('word_count', 0)}, Sentences: {stats.get('sentence_count', 0)}")
    
    # Show top words
    print(f"\nTop 10 most frequent words:")
    top_words = processor.get_top_words(10)
    for word, count in top_words:
        print(f"  {word}: {count}")
    
    # Generate summary report
    print(f"\nSummary Report:")
    print(processor.generate_summary_report())


def main():
    """Main function with menu-driven interface."""
    processor = TextProcessor()
    
    while True:
        print("\n=== Text Processing Pipeline ===")
        print("1. Process text string")
        print("2. Process single file")
        print("3. Process directory")
        print("4. Show top words")
        print("5. Search word contexts")
        print("6. Generate summary report")
        print("7. Show reading statistics")
        print("8. Filter words by length")
        print("9. Run demonstration")
        print("10. Exit")
        print("=" * 35)
        
        choice = input("Enter your choice (1-10): ").strip()
        
        if choice == "1":
            # TODO: Implement process text string functionality
            pass
            
        elif choice == "2":
            # TODO: Implement process single file functionality
            pass
            
        elif choice == "3":
            # TODO: Implement process directory functionality
            pass
            
        elif choice == "4":
            # TODO: Implement show top words functionality
            pass
            
        elif choice == "5":
            # TODO: Implement search word contexts functionality
            pass
            
        elif choice == "6":
            # TODO: Implement generate summary report functionality
            pass
            
        elif choice == "7":
            # TODO: Implement show reading statistics functionality
            pass
            
        elif choice == "8":
            # TODO: Implement filter words by length functionality
            pass
            
        elif choice == "9":
            demonstrate_text_processing()
            
        elif choice == "10":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()