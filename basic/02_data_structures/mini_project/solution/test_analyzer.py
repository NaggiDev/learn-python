"""
Test cases for the TextAnalyzer class.
"""

import unittest
from text_analyzer import TextAnalyzer


class TestTextAnalyzer(unittest.TestCase):
    """Test cases for the TextAnalyzer class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.sample_text = """Hello, world! This is a test.
        
        This is another paragraph. It contains multiple sentences. How many? Three!
        
        Short paragraph."""
        
        self.analyzer = TextAnalyzer(self.sample_text)
    
    def test_word_count(self):
        """Test word count calculation."""
        self.assertEqual(self.analyzer.get_word_count(), 19)
    
    def test_character_count(self):
        """Test character count calculation."""
        self.assertEqual(self.analyzer.get_character_count(), 115)
        self.assertEqual(self.analyzer.get_character_count(include_spaces=False), 86)
    
    def test_sentence_count(self):
        """Test sentence count calculation."""
        self.assertEqual(self.analyzer.get_sentence_count(), 6)
    
    def test_paragraph_count(self):
        """Test paragraph count calculation."""
        self.assertEqual(self.analyzer.get_paragraph_count(), 3)
    
    def test_average_word_length(self):
        """Test average word length calculation."""
        self.assertAlmostEqual(self.analyzer.get_average_word_length(), 4.0, places=1)
    
    def test_average_sentence_length(self):
        """Test average sentence length calculation."""
        self.assertAlmostEqual(self.analyzer.get_average_sentence_length(), 3.17, places=2)
    
    def test_most_common_words(self):
        """Test most common words calculation."""
        most_common = self.analyzer.get_most_common_words(3)
        self.assertEqual(len(most_common), 3)
        # Check that the most common word is "this"
        self.assertEqual(most_common[0][0], "this")
        self.assertEqual(most_common[0][1], 3)
    
    def test_least_common_words(self):
        """Test least common words calculation."""
        least_common = self.analyzer.get_least_common_words(5)
        self.assertEqual(len(least_common), 5)
        # All least common words should appear only once
        for word, count in least_common:
            self.assertEqual(count, 1)
    
    def test_unique_words_count(self):
        """Test unique words count calculation."""
        self.assertEqual(self.analyzer.get_unique_words_count(), 17)
    
    def test_word_frequency(self):
        """Test word frequency calculation."""
        freq = self.analyzer.get_word_frequency()
        self.assertEqual(freq["this"], 3)
        self.assertEqual(freq["paragraph"], 2)
        self.assertEqual(freq["hello"], 1)
    
    def test_character_frequency(self):
        """Test character frequency calculation."""
        freq = self.analyzer.get_character_frequency()
        self.assertEqual(freq["a"], 7)
        self.assertEqual(freq["t"], 7)
        self.assertEqual(freq["h"], 5)
    
    def test_character_percentage(self):
        """Test character percentage calculation."""
        percentages = self.analyzer.get_character_percentage()
        self.assertAlmostEqual(percentages["alphabetic"], 74.8, places=1)
        self.assertAlmostEqual(percentages["numeric"], 0.0, places=1)
        self.assertAlmostEqual(percentages["special"], 10.4, places=1)
        self.assertAlmostEqual(percentages["whitespace"], 14.8, places=1)
    
    def test_readability_score(self):
        """Test readability score calculation."""
        score = self.analyzer.calculate_readability_score()
        self.assertGreater(score, 0)
    
    def test_find_word(self):
        """Test finding word occurrences."""
        occurrences = self.analyzer.find_word("paragraph")
        self.assertEqual(len(occurrences), 2)
    
    def test_count_word(self):
        """Test counting word occurrences."""
        self.assertEqual(self.analyzer.count_word("this"), 3)
        self.assertEqual(self.analyzer.count_word("paragraph"), 2)
        self.assertEqual(self.analyzer.count_word("nonexistent"), 0)


if __name__ == "__main__":
    unittest.main()