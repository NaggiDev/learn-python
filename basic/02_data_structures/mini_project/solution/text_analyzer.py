"""
Text Analyzer

This module provides functionality to analyze text and extract various statistics.
"""

import re
import string
from collections import Counter


class TextAnalyzer:
    """
    A class for analyzing text and extracting various statistics.
    """
    
    def __init__(self, text):
        """
        Initialize the TextAnalyzer with the given text.
        
        Args:
            text (str): The text to analyze
        """
        self.text = text
        self.words = self._extract_words()
        self.sentences = self._extract_sentences()
        self.paragraphs = self._extract_paragraphs()
        
    def _extract_words(self):
        """
        Extract words from the text.
        
        Returns:
            list: A list of words
        """
        # Convert to lowercase and remove punctuation
        text_lower = self.text.lower()
        # Replace punctuation with spaces
        for char in string.punctuation:
            text_lower = text_lower.replace(char, ' ')
        # Split by whitespace and filter out empty strings
        words = [word for word in text_lower.split() if word]
        return words
    
    def _extract_sentences(self):
        """
        Extract sentences from the text.
        
        Returns:
            list: A list of sentences
        """
        # Split by sentence terminators and filter out empty strings
        pattern = r'[.!?]+(?=\s|\Z)'
        sentences = re.split(pattern, self.text)
        return [s.strip() for s in sentences if s.strip()]
    
    def _extract_paragraphs(self):
        """
        Extract paragraphs from the text.
        
        Returns:
            list: A list of paragraphs
        """
        # Split by double newlines and filter out empty strings
        paragraphs = re.split(r'\n\s*\n', self.text)
        return [p.strip() for p in paragraphs if p.strip()]
    
    def get_word_count(self):
        """
        Get the total number of words in the text.
        
        Returns:
            int: The number of words
        """
        return len(self.words)
    
    def get_character_count(self, include_spaces=True):
        """
        Get the total number of characters in the text.
        
        Args:
            include_spaces (bool): Whether to include whitespace in the count
            
        Returns:
            int: The number of characters
        """
        if include_spaces:
            return len(self.text)
        else:
            return len(self.text.replace(" ", "").replace("\n", "").replace("\t", ""))
    
    def get_sentence_count(self):
        """
        Get the total number of sentences in the text.
        
        Returns:
            int: The number of sentences
        """
        return len(self.sentences)
    
    def get_paragraph_count(self):
        """
        Get the total number of paragraphs in the text.
        
        Returns:
            int: The number of paragraphs
        """
        return len(self.paragraphs)
    
    def get_average_word_length(self):
        """
        Calculate the average word length.
        
        Returns:
            float: The average word length
        """
        if not self.words:
            return 0
        total_length = sum(len(word) for word in self.words)
        return total_length / len(self.words)
    
    def get_average_sentence_length(self):
        """
        Calculate the average sentence length in words.
        
        Returns:
            float: The average sentence length
        """
        if not self.sentences:
            return 0
        
        # Count words in each sentence
        sentence_lengths = []
        for sentence in self.sentences:
            # Remove punctuation and split by whitespace
            cleaned = ''.join(c if c not in string.punctuation else ' ' for c in sentence)
            words = [word for word in cleaned.split() if word]
            sentence_lengths.append(len(words))
        
        return sum(sentence_lengths) / len(self.sentences)
    
    def get_most_common_words(self, n=10):
        """
        Get the most common words in the text.
        
        Args:
            n (int): The number of words to return
            
        Returns:
            list: A list of (word, count) tuples
        """
        word_counts = Counter(self.words)
        return word_counts.most_common(n)
    
    def get_least_common_words(self, n=10):
        """
        Get the least common words in the text.
        
        Args:
            n (int): The number of words to return
            
        Returns:
            list: A list of (word, count) tuples
        """
        word_counts = Counter(self.words)
        return word_counts.most_common()[:-n-1:-1]
    
    def get_unique_words_count(self):
        """
        Get the number of unique words in the text.
        
        Returns:
            int: The number of unique words
        """
        return len(set(self.words))
    
    def get_word_frequency(self):
        """
        Get the frequency of each word in the text.
        
        Returns:
            dict: A dictionary mapping words to their frequencies
        """
        return dict(Counter(self.words))
    
    def get_character_frequency(self):
        """
        Get the frequency of each character in the text.
        
        Returns:
            dict: A dictionary mapping characters to their frequencies
        """
        return dict(Counter(self.text))
    
    def get_character_percentage(self):
        """
        Calculate the percentage of alphabetic, numeric, and special characters.
        
        Returns:
            dict: A dictionary with keys 'alphabetic', 'numeric', 'special', and 'whitespace'
        """
        total_chars = len(self.text)
        if total_chars == 0:
            return {
                'alphabetic': 0,
                'numeric': 0,
                'special': 0,
                'whitespace': 0
            }
        
        alphabetic = sum(1 for c in self.text if c.isalpha())
        numeric = sum(1 for c in self.text if c.isdigit())
        whitespace = sum(1 for c in self.text if c.isspace())
        special = total_chars - alphabetic - numeric - whitespace
        
        return {
            'alphabetic': (alphabetic / total_chars) * 100,
            'numeric': (numeric / total_chars) * 100,
            'special': (special / total_chars) * 100,
            'whitespace': (whitespace / total_chars) * 100
        }
    
    def calculate_readability_score(self):
        """
        Calculate a simple readability score based on word and sentence length.
        
        Returns:
            float: A readability score (higher means more complex)
        """
        avg_word_length = self.get_average_word_length()
        avg_sentence_length = self.get_average_sentence_length()
        
        # Simple formula: weighted average of word length and sentence length
        return (avg_word_length * 0.5) + (avg_sentence_length * 0.5)
    
    def find_word(self, word):
        """
        Find all occurrences of a word in the text.
        
        Args:
            word (str): The word to search for
            
        Returns:
            list: A list of indices where the word occurs
        """
        word = word.lower()
        text_lower = self.text.lower()
        
        # Use regex to find word boundaries
        pattern = r'\b' + re.escape(word) + r'\b'
        matches = re.finditer(pattern, text_lower)
        
        return [match.start() for match in matches]
    
    def count_word(self, word):
        """
        Count occurrences of a word in the text.
        
        Args:
            word (str): The word to count
            
        Returns:
            int: The number of occurrences
        """
        word = word.lower()
        return self.words.count(word)
    
    def generate_summary(self):
        """
        Generate a summary of the text analysis.
        
        Returns:
            str: A formatted summary
        """
        summary = "=== Text Analysis Summary ===\n\n"
        
        # Basic statistics
        summary += "Basic Statistics:\n"
        summary += f"- Word count: {self.get_word_count()}\n"
        summary += f"- Character count (with spaces): {self.get_character_count()}\n"
        summary += f"- Character count (without spaces): {self.get_character_count(include_spaces=False)}\n"
        summary += f"- Sentence count: {self.get_sentence_count()}\n"
        summary += f"- Paragraph count: {self.get_paragraph_count()}\n"
        summary += f"- Average word length: {self.get_average_word_length():.2f} characters\n"
        summary += f"- Average sentence length: {self.get_average_sentence_length():.2f} words\n\n"
        
        # Word analysis
        summary += "Word Analysis:\n"
        summary += f"- Unique words: {self.get_unique_words_count()}\n"
        
        summary += "- Most common words:\n"
        for word, count in self.get_most_common_words(5):
            summary += f"  * {word}: {count}\n"
        
        summary += "- Least common words:\n"
        for word, count in self.get_least_common_words(5):
            summary += f"  * {word}: {count}\n\n"
        
        # Character analysis
        summary += "Character Analysis:\n"
        char_percentage = self.get_character_percentage()
        summary += f"- Alphabetic: {char_percentage['alphabetic']:.2f}%\n"
        summary += f"- Numeric: {char_percentage['numeric']:.2f}%\n"
        summary += f"- Special: {char_percentage['special']:.2f}%\n"
        summary += f"- Whitespace: {char_percentage['whitespace']:.2f}%\n\n"
        
        # Readability
        summary += "Readability:\n"
        score = self.calculate_readability_score()
        summary += f"- Score: {score:.2f}\n"
        
        if score < 5:
            difficulty = "Easy"
        elif score < 10:
            difficulty = "Moderate"
        else:
            difficulty = "Difficult"
        
        summary += f"- Difficulty: {difficulty}\n"
        
        return summary


def main():
    """
    Main function to demonstrate the TextAnalyzer.
    """
    # Read sample text
    try:
        with open("sample_text.txt", "r", encoding="utf-8") as file:
            sample_text = file.read()
    except FileNotFoundError:
        sample_text = """
        This is a sample text. It contains multiple sentences, some of which are short.
        Others are longer and more complex, with multiple clauses and phrases.
        
        This is a new paragraph. It adds more content to analyze.
        """
    
    # Create analyzer
    analyzer = TextAnalyzer(sample_text)
    
    # Print summary
    print(analyzer.generate_summary())
    
    # Interactive mode
    print("\n=== Interactive Mode ===")
    print("Enter a word to search for (or 'exit' to quit):")
    
    while True:
        query = input("> ").strip().lower()
        if query == "exit":
            break
        
        count = analyzer.count_word(query)
        print(f"'{query}' appears {count} times in the text.")


if __name__ == "__main__":
    main()