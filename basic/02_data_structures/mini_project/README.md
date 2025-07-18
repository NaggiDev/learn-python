# Text Analyzer Mini-Project

## Overview

In this mini-project, you will build a text analyzer tool that processes text and provides various statistics and insights about the content. This project will help you apply the data structure concepts you've learned, particularly working with strings, lists, dictionaries, and sets.

## Learning Objectives

By completing this project, you will:

1. Apply string manipulation techniques to process text data
2. Use dictionaries to count and store word frequencies
3. Implement sets to identify unique words and characters
4. Practice list operations for sorting and filtering results
5. Combine multiple data structures to solve a complex problem
6. Develop a command-line interface for user interaction

## Project Requirements

Your text analyzer should provide the following functionality:

1. **Basic Text Statistics:**
   - Word count
   - Character count (with and without spaces)
   - Sentence count
   - Paragraph count
   - Average word length
   - Average sentence length (in words)

2. **Word Analysis:**
   - Most common words
   - Least common words
   - Unique words count
   - Word frequency distribution

3. **Character Analysis:**
   - Character frequency distribution
   - Percentage of alphabetic, numeric, and special characters

4. **Readability Metrics:**
   - Calculate a simple readability score based on word and sentence length

5. **Search Functionality:**
   - Find all occurrences of a specific word or phrase
   - Count occurrences of a specific word or phrase

## Project Structure

The starter code provides the basic structure for your text analyzer:

```
mini_project/
├── starter_code/
│   ├── text_analyzer.py     # Main implementation file
│   ├── test_analyzer.py     # Test cases for your implementation
│   └── sample_text.txt      # Sample text for testing
└── solution/
    ├── text_analyzer.py     # Reference solution
    ├── test_analyzer.py     # Test cases
    └── sample_text.txt      # Sample text for testing
```

## Implementation Guidelines

1. Start by implementing the basic text statistics functions
2. Move on to word analysis, using dictionaries to store word frequencies
3. Implement character analysis using similar techniques
4. Add the readability metrics calculation
5. Finally, implement the search functionality

## Testing Your Implementation

The provided `test_analyzer.py` file contains test cases to verify your implementation. Run the tests to check if your code meets the requirements:

```
python test_analyzer.py
```

## Bonus Challenges

If you complete the basic requirements, try these bonus challenges:

1. **Advanced Readability Metrics:**
   - Implement more sophisticated readability formulas like Flesch-Kincaid or SMOG
   
2. **Sentiment Analysis:**
   - Add basic sentiment analysis to determine if the text is positive, negative, or neutral
   
3. **Word Cloud Generation:**
   - Generate a simple ASCII word cloud based on word frequencies
   
4. **File Input/Output:**
   - Allow the analyzer to read from and write results to files

## Submission

Your submission should include:

1. Your completed `text_analyzer.py` file
2. Any additional files you created for the project
3. A brief report explaining your implementation choices and any challenges you faced

## Evaluation Criteria

Your project will be evaluated based on:

1. Correctness: Does your code produce the expected results?
2. Code quality: Is your code well-organized, commented, and efficient?
3. Completeness: Did you implement all the required functionality?
4. Creativity: Did you find interesting ways to solve the problems?

Good luck with your text analyzer project!