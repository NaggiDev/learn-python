"""
Exercise 5: Code Quality Tools Practice

This file contains intentionally poor-quality code that violates various
style guidelines and best practices. Your task is to:

1. Run various code quality tools on this file
2. Fix the issues identified by the tools
3. Set up proper configuration files
4. Practice using different tools

Instructions:
1. Install the required tools:
   pip install pylint flake8 black isort mypy bandit

2. Run each tool on this file and observe the output:
   pylint 05_code_quality_practice.py
   flake8 05_code_quality_practice.py
   black --diff 05_code_quality_practice.py
   isort --diff 05_code_quality_practice.py
   mypy 05_code_quality_practice.py
   bandit 05_code_quality_practice.py

3. Fix the issues and re-run the tools

Note: This file intentionally contains many style violations and issues!
"""

# Imports are not sorted and have issues
import json
import sys
from collections import defaultdict
import os
from typing import Dict
import random
from typing import List
import requests


# Global variables with poor naming
userName = "admin"
PASSWORD = "password123"  # Security issue: hardcoded password
maxRetries = 5


# Function with many style violations
def calculateUserScore(user_data,bonus_points=0,penalty_points=0,):
    """Calculate user score with bonus and penalty."""
    # Poor variable naming and formatting
    totalScore=0
    if user_data==None:
        return 0
    
    # Long line that exceeds recommended length
    base_score = user_data.get("base_score", 0) + bonus_points - penalty_points + random.randint(1, 100)
    
    # Unused variable
    temp_var = "unused"
    
    # Poor error handling
    try:
        totalScore=base_score*1.5
    except:
        totalScore=0
    
    return totalScore


# Class with style issues
class userAccount:
    def __init__(self,username,email,age):
        self.username=username
        self.email=email
        self.age=age
        self._balance=0.0
    
    # Method with no docstring and poor formatting
    def deposit(self,amount):
        if amount>0:
            self._balance+=amount
            return True
        else:
            return False
    
    # Method with security issue
    def authenticate(self, password):
        # Security issue: using == for password comparison
        if password == PASSWORD:
            return True
        return False
    
    # Method with type annotation issues
    def get_user_info(self) -> dict:
        return {
            "username": self.username,
            "email": self.email,
            "age": self.age,
            "balance": self._balance
        }


# Function with SQL injection vulnerability
def get_user_by_id(user_id):
    """Get user from database by ID."""
    # Security issue: SQL injection vulnerability
    query = "SELECT * FROM users WHERE id = " + str(user_id)
    # This would execute the query in a real application
    return query


# Function with poor error handling and formatting
def process_api_data(url,headers=None):
    """Process data from API."""
    if headers==None:
        headers={}
    
    # Poor exception handling
    try:
        response=requests.get(url,headers=headers)
        data=response.json()
        
        # Poor variable naming and logic
        result=[]
        for item in data:
            if item['status']=='active':
                result.append(item)
        
        return result
    except:
        return []


# Function with complexity issues
def complex_calculation(data, option1=True, option2=False, option3=None, option4="default", option5=0, option6=1.0, option7=[], option8={}):
    """Function with too many parameters and complexity."""
    if option3 is None:
        option3 = []
    
    result = 0
    
    if option1:
        if option2:
            if option4 == "special":
                if option5 > 0:
                    if option6 > 1.0:
                        if len(option7) > 0:
                            if len(option8) > 0:
                                for item in data:
                                    if item > 0:
                                        result += item * option6
                                    else:
                                        result -= item
                            else:
                                result = sum(data)
                        else:
                            result = len(data)
                    else:
                        result = max(data) if data else 0
                else:
                    result = min(data) if data else 0
            else:
                result = sum(data) / len(data) if data else 0
        else:
            result = sum(data)
    else:
        result = 0
    
    return result


# Function with type annotation issues
def merge_dictionaries(dict1, dict2):
    """Merge two dictionaries."""
    result = dict1.copy()
    result.update(dict2)
    return result


# Function using dangerous built-ins
def execute_user_code(code_string):
    """Execute user-provided code."""
    # Security issue: using eval
    return eval(code_string)


# Function with poor naming and logic
def func1(x):
    """Function with poor naming."""
    if x:
        return True
    else:
        return False


# Class with too few public methods
class DataContainer:
    def __init__(self, data):
        self._data = data


# Function with unused imports and variables
def process_file_data():
    """Process file data."""
    # os and sys are imported but not used in this function
    data = [1, 2, 3, 4, 5]
    unused_var = "not used"
    
    return sum(data)


# Function with mutable default argument
def add_to_list(item, target_list=[]):
    """Add item to list."""
    target_list.append(item)
    return target_list


# Function with inconsistent return types
def get_value(key, data):
    """Get value from data."""
    if key in data:
        return data[key]
    else:
        return None


# Main function with poor structure
def main():
    """Main function."""
    print("Starting application...")
    
    # Create user account
    user=userAccount("john_doe","john@example.com",25)
    
    # Calculate score
    user_data={"base_score":100}
    score=calculateUserScore(user_data,10,5)
    
    print(f"User score: {score}")
    
    # Process API data (this would fail in real usage)
    api_data=process_api_data("https://api.example.com/data")
    print(f"API data items: {len(api_data)}")
    
    # Demonstrate security issues
    user_code="print('Hello from eval!')"
    result=execute_user_code(user_code)
    
    print("Application finished.")


if __name__=="__main__":
    main()


# TODO: After running the tools, create the following configuration files:

# 1. .pylintrc - Configure pylint settings
# 2. .flake8 - Configure flake8 settings  
# 3. pyproject.toml - Configure black and isort
# 4. mypy.ini - Configure mypy settings

# Example configurations are provided in the solution file.