"""
Text Processing Pipeline - Solution

This solution demonstrates advanced text processing while using basic Python concepts,
preparing students for intermediate topics like functional programming and data analysis.
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
        self.all_texts = []  # Store processed texts for context search
        
    def clean_text(self, text: str) -> str:
        """Clean and normalize text for processing."""
        # Convert to lowercase
        text = text.lower()
        
        # Replace multiple whitespace with single space
        text = re.sub(r'\s+', ' ', text)
        
        # Remove extra punctuation but keep sentence endings
        text = re.sub(r'[^\w\s.!?]', ' ', text)
        
        # Clean up spaces around punctuation
        text = re.sub(r'\s+([.!?])', r'\1', text)
        
        return text.strip()
    
    def extract_words(self, text: str) -> List[str]:
        """Extract words from cleaned text."""
        # Remove punctuation and split into words
        translator = str.maketrans('', '', string.punctuation)
        clean_text = text.translate(translator)
        
        # Split and filter empty strings
        words = [word.strip() for word in clean_text.split() if word.strip()]
        
        return words
    
    def extract_sentences(self, text: str) -> List[str]:
        """Extract sentences from text."""
        # Split on sentence endings
        sentences = re.split(r'[.!?]+', text)
        
        # Clean up sentences
        sentences = [s.strip() for s in sentences if s.strip()]
        
        return sentences
    
    def process_text(self, text: str, source_name: str = "string_input") -> Dict:
        """Process a single text and update statistics."""
        if not text.strip():
            return {"word_count": 0, "sentence_count": 0, "char_count": 0}
        
        # Store original text for context search
        self.all_texts.append((source_name, text))
        
        # Clean text
        cleaned_text = self.clean_text(text)
        
        # Extract words and sentences
        words = self.extract_words(cleaned_text)
        sentences = self.extract_sentences(text)
        
        # Update word frequencies
        for word in words:
            if len(word) > 1:  # Skip single characters
                self.word_frequencies[word] += 1
        
        # Calculate statistics
        stats = {
            "word_count": len(words),
            "sentence_count": len(sentences),
            "char_count": len(text),
            "unique_words": len(set(words)),
            "avg_word_length": sum(len(word) for word in words) / len(words) if words else 0,
            "avg_sentence_length": len(words) / len(sentences) if sentences else 0
        }
        
        # Store file statistics
        self.file_stats[source_name] = stats
        
        return stats
    
    def process_file(self, filepath: str) -> bool:
        """Process a single text file."""
        try:
            # Try different encodings
            encodings = ['utf-8', 'latin-1', 'cp1252']
            text = None
            
            for encoding in encodings:
                try:
                    with open(filepath, 'r', encoding=encoding) as file:
                        text = file.read()
                    break
                except UnicodeDecodeError:
                    continue
            
            if text is None:
                print(f"Could not read file {filepath} with any encoding")
                return False
            
            # Process the text
            filename = os.path.basename(filepath)
            self.process_text(text, filename)
            self.processed_files.append(filepath)
            
            return True
            
        except Exception as e:
            print(f"Error processing file {filepath}: {e}")
            return False
    
    def process_directory(self, directory_path: str, file_extensions: List[str] = None) -> int:
        """Process all text files in a directory."""
        if file_extensions is None:
            file_extensions = ['.txt', '.md', '.py', '.html', '.css', '.js']
        
        if not os.path.exists(directory_path):
            print(f"Directory {directory_path} does not exist")
            return 0
        
        processed_count = 0
        
        try:
            for filename in os.listdir(directory_path):
                filepath = os.path.join(directory_path, filename)
                
                if os.path.isfile(filepath):
                    # Check file extension
                    _, ext = os.path.splitext(filename)
                    if ext.lower() in file_extensions:
                        if self.process_file(filepath):
                            processed_count += 1
                            
        except Exception as e:
            print(f"Error accessing directory {directory_path}: {e}")
        
        return processed_count
    
    def get_top_words(self, n: int = 10) -> List[Tuple[str, int]]:
        """Get the top N most frequent words."""
        # Sort by frequency (descending) and then alphabetically
        sorted_words = sorted(
            self.word_frequencies.items(),
            key=lambda x: (-x[1], x[0])
        )
        
        return sorted_words[:n]
    
    def search_word_contexts(self, word: str, context_size: int = 5) -> List[str]:
        """Find contexts where a specific word appears."""
        contexts = []
        word_lower = word.lower()
        
        for source_name, text in self.all_texts:
            words = self.extract_words(self.clean_text(text))
            
            for i, w in enumerate(words):
                if w == word_lower:
                    # Extract context
                    start = max(0, i - context_size)
                    end = min(len(words), i + context_size + 1)
                    context_words = words[start:end]
                    
                    # Highlight the target word
                    context_words[i - start] = f"**{context_words[i - start]}**"
                    
                    context = " ".join(context_words)
                    contexts.append(f"[{source_name}] ...{context}...")
        
        return contexts
    
    def generate_summary_report(self) -> str:
        """Generate a comprehensive summary report."""
        if not self.file_stats:
            return "No texts have been processed yet."
        
        report_lines = ["Text Processing Summary Report", "=" * 50]
        
        # Overall statistics
        total_words = sum(stats["word_count"] for stats in self.file_stats.values())
        total_sentences = sum(stats["sentence_count"] for stats in self.file_stats.values())
        total_chars = sum(stats["char_count"] for stats in self.file_stats.values())
        unique_words = len(self.word_frequencies)
        
        report_lines.extend([
            f"Files processed: {len(self.file_stats)}",
            f"Total words: {total_words:,}",
            f"Total sentences: {total_sentences:,}",
            f"Total characters: {total_chars:,}",
            f"Unique words: {unique_words:,}",
            f"Average words per sentence: {total_words / total_sentences if total_sentences > 0 else 0:.2f}",
            ""
        ])
        
        # Top words
        report_lines.append("Top 10 Most Frequent Words:")
        report_lines.append("-" * 30)
        top_words = self.get_top_words(10)
        for word, count in top_words:
            percentage = (count / total_words) * 100 if total_words > 0 else 0
            report_lines.append(f"{word:<15}: {count:>5} ({percentage:.1f}%)")
        
        report_lines.append("")
        
        # Per-file statistics
        if len(self.file_stats) > 1:
            report_lines.append("Per-File Statistics:")
            report_lines.append("-" * 50)
            for filename, stats in self.file_stats.items():
                report_lines.append(f"{filename}:")
                report_lines.append(f"  Words: {stats['word_count']:,}")
                report_lines.append(f"  Sentences: {stats['sentence_count']:,}")
                report_lines.append(f"  Unique words: {stats['unique_words']:,}")
                report_lines.append(f"  Avg word length: {stats['avg_word_length']:.1f}")
                report_lines.append("")
        
        return "\n".join(report_lines)
    
    def get_reading_statistics(self) -> Dict:
        """Calculate reading-related statistics."""
        if not self.file_stats:
            return {}
        
        total_words = sum(stats["word_count"] for stats in self.file_stats.values())
        total_sentences = sum(stats["sentence_count"] for stats in self.file_stats.values())
        
        # Reading time estimation (200 words per minute)
        reading_time_minutes = total_words / 200
        
        # Text complexity (based on average sentence length)
        avg_sentence_length = total_words / total_sentences if total_sentences > 0 else 0
        
        if avg_sentence_length < 10:
            complexity = "Simple"
        elif avg_sentence_length < 20:
            complexity = "Moderate"
        else:
            complexity = "Complex"
        
        return {
            "total_words": total_words,
            "estimated_reading_time_minutes": reading_time_minutes,
            "estimated_reading_time_formatted": f"{int(reading_time_minutes)}m {int((reading_time_minutes % 1) * 60)}s",
            "average_sentence_length": avg_sentence_length,
            "text_complexity": complexity,
            "vocabulary_richness": len(self.word_frequencies) / total_words if total_words > 0 else 0
        }
    
    def filter_words_by_length(self, min_length: int, max_length: int = None) -> Dict[str, int]:
        """Filter words by length and return their frequencies."""
        filtered_words = {}
        
        for word, count in self.word_frequencies.items():
            word_length = len(word)
            if word_length >= min_length:
                if max_length is None or word_length <= max_length:
                    filtered_words[word] = count
        
        return filtered_words
    
    def find_common_patterns(self) -> Dict[str, List[str]]:
        """Find common patterns in the text."""
        patterns = {
            "common_prefixes": [],
            "common_suffixes": [],
            "long_words": [],
            "repeated_patterns": []
        }
        
        words = list(self.word_frequencies.keys())
        
        # Find common prefixes (3+ characters)
        prefix_counts = defaultdict(int)
        for word in words:
            if len(word) >= 5:
                for i in range(3, min(6, len(word))):
                    prefix = word[:i]
                    prefix_counts[prefix] += 1
        
        patterns["common_prefixes"] = [
            prefix for prefix, count in prefix_counts.items() 
            if count >= 3
        ][:10]
        
        # Find common suffixes (3+ characters)
        suffix_counts = defaultdict(int)
        for word in words:
            if len(word) >= 5:
                for i in range(3, min(6, len(word))):
                    suffix = word[-i:]
                    suffix_counts[suffix] += 1
        
        patterns["common_suffixes"] = [
            suffix for suffix, count in suffix_counts.items() 
            if count >= 3
        ][:10]
        
        # Find long words (8+ characters)
        patterns["long_words"] = [
            word for word in words if len(word) >= 8
        ][:20]
        
        return patterns


def demonstrate_text_processing():
    """Demonstrate the text processing capabilities."""
    processor = TextProcessor()
    
    # Sample texts for demonstration
    sample_texts = [
        "The quick brown fox jumps over the lazy dog. This is a sample sentence for testing. The fox is very quick and brown.",
        "Python is a powerful programming language. It is used for web development, data analysis, and more. Programming with Python is enjoyable.",
        "Text processing is an important skill in programming. Regular expressions are very useful for this task. Processing text efficiently requires practice."
    ]
    
    print("Text Processing Pipeline Demonstration")
    print("=" * 50)
    
    # Process sample texts
    for i, text in enumerate(sample_texts, 1):
        print(f"\nProcessing sample text {i}...")
        stats = processor.process_text(text, f"sample_{i}")
        print(f"Words: {stats['word_count']}, Sentences: {stats['sentence_count']}")
        print(f"Unique words: {stats['unique_words']}, Avg word length: {stats['avg_word_length']:.1f}")
    
    # Show top words
    print(f"\nTop 10 most frequent words:")
    top_words = processor.get_top_words(10)
    for word, count in top_words:
        print(f"  {word}: {count}")
    
    # Show reading statistics
    reading_stats = processor.get_reading_statistics()
    print(f"\nReading Statistics:")
    print(f"  Estimated reading time: {reading_stats['estimated_reading_time_formatted']}")
    print(f"  Text complexity: {reading_stats['text_complexity']}")
    print(f"  Vocabulary richness: {reading_stats['vocabulary_richness']:.3f}")
    
    # Search for word contexts
    print(f"\nContexts for word 'python':")
    contexts = processor.search_word_contexts("python", 3)
    for context in contexts[:3]:
        print(f"  {context}")


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
            text = input("Enter text to process: ")
            if text.strip():
                stats = processor.process_text(text)
                print(f"Processed: {stats['word_count']} words, {stats['sentence_count']} sentences")
            
        elif choice == "2":
            filepath = input("Enter file path: ").strip()
            if processor.process_file(filepath):
                print(f"Successfully processed {filepath}")
            else:
                print("Failed to process file")
            
        elif choice == "3":
            directory = input("Enter directory path: ").strip()
            count = processor.process_directory(directory)
            print(f"Processed {count} files from {directory}")
            
        elif choice == "4":
            try:
                n = int(input("Number of top words to show (default 10): ") or "10")
                top_words = processor.get_top_words(n)
                if top_words:
                    print(f"\nTop {n} words:")
                    for word, count in top_words:
                        print(f"  {word}: {count}")
                else:
                    print("No words processed yet.")
            except ValueError:
                print("Please enter a valid number.")
            
        elif choice == "5":
            word = input("Enter word to search: ").strip()
            if word:
                contexts = processor.search_word_contexts(word)
                if contexts:
                    print(f"\nContexts for '{word}':")
                    for context in contexts[:10]:  # Limit to 10 results
                        print(f"  {context}")
                else:
                    print(f"No contexts found for '{word}'")
            
        elif choice == "6":
            report = processor.generate_summary_report()
            print("\n" + report)
            
        elif choice == "7":
            stats = processor.get_reading_statistics()
            if stats:
                print("\nReading Statistics:")
                print(f"  Total words: {stats['total_words']:,}")
                print(f"  Reading time: {stats['estimated_reading_time_formatted']}")
                print(f"  Average sentence length: {stats['average_sentence_length']:.1f} words")
                print(f"  Text complexity: {stats['text_complexity']}")
                print(f"  Vocabulary richness: {stats['vocabulary_richness']:.3f}")
            else:
                print("No texts processed yet.")
            
        elif choice == "8":
            try:
                min_len = int(input("Minimum word length: "))
                max_len_input = input("Maximum word length (press Enter for no limit): ").strip()
                max_len = int(max_len_input) if max_len_input else None
                
                filtered = processor.filter_words_by_length(min_len, max_len)
                if filtered:
                    print(f"\nWords with length {min_len}-{max_len or 'unlimited'}:")
                    sorted_filtered = sorted(filtered.items(), key=lambda x: -x[1])
                    for word, count in sorted_filtered[:20]:  # Show top 20
                        print(f"  {word} ({len(word)} chars): {count}")
                else:
                    print("No words found in the specified length range.")
            except ValueError:
                print("Please enter valid numbers.")
            
        elif choice == "9":
            demonstrate_text_processing()
            
        elif choice == "10":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()