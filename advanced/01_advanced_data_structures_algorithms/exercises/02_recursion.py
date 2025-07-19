"""
Recursion Exercises

This file contains exercises to practice recursive problem-solving techniques.
Each exercise focuses on different aspects of recursion: basic recursion,
optimization, backtracking, and divide-and-conquer.

Instructions:
1. Implement each recursive function according to the specifications
2. Pay attention to base cases and recursive cases
3. Consider optimization opportunities where noted
4. Run the tests to verify your implementations
"""

from typing import List, Optional, Tuple, Any


# Exercise 1: Basic Recursion
def exercise_1_basic_recursion():
    """
    Implement basic recursive functions to build foundational understanding.
    """
    
    # TODO: Implement recursive power function
    def power(base: int, exponent: int) -> int:
        """
        Calculate base^exponent using recursion.
        
        Args:
            base: The base number
            exponent: The exponent (non-negative integer)
        
        Returns:
            base raised to the power of exponent
        
        Examples:
            power(2, 3) -> 8
            power(5, 0) -> 1
            power(3, 4) -> 81
        """
        # TODO: Implement recursive power calculation
        pass
    
    # TODO: Implement recursive sum of digits
    def sum_of_digits(n: int) -> int:
        """
        Calculate the sum of digits in a number using recursion.
        
        Args:
            n: A non-negative integer
        
        Returns:
            Sum of all digits in n
        
        Examples:
            sum_of_digits(123) -> 6 (1 + 2 + 3)
            sum_of_digits(456) -> 15 (4 + 5 + 6)
            sum_of_digits(0) -> 0
        """
        # TODO: Implement recursive digit sum
        pass
    
    # TODO: Implement recursive palindrome checker
    def is_palindrome(s: str) -> bool:
        """
        Check if a string is a palindrome using recursion.
        
        Args:
            s: String to check
        
        Returns:
            True if s is a palindrome, False otherwise
        
        Examples:
            is_palindrome("racecar") -> True
            is_palindrome("hello") -> False
            is_palindrome("a") -> True
        """
        # TODO: Implement recursive palindrome check
        pass
    
    # TODO: Implement recursive GCD (Greatest Common Divisor)
    def gcd(a: int, b: int) -> int:
        """
        Find the greatest common divisor using Euclidean algorithm (recursive).
        
        Args:
            a: First positive integer
            b: Second positive integer
        
        Returns:
            Greatest common divisor of a and b
        
        Examples:
            gcd(48, 18) -> 6
            gcd(17, 13) -> 1
            gcd(100, 25) -> 25
        """
        # TODO: Implement recursive GCD using Euclidean algorithm
        pass


# Exercise 2: List and Array Recursion
def exercise_2_list_recursion():
    """
    Practice recursion with lists and arrays.
    """
    
    # TODO: Implement recursive list reversal
    def reverse_list(arr: List[Any]) -> List[Any]:
        """
        Reverse a list using recursion.
        
        Args:
            arr: List to reverse
        
        Returns:
            New list with elements in reverse order
        
        Examples:
            reverse_list([1, 2, 3, 4]) -> [4, 3, 2, 1]
            reverse_list(['a', 'b', 'c']) -> ['c', 'b', 'a']
            reverse_list([]) -> []
        """
        # TODO: Implement recursive list reversal
        pass
    
    # TODO: Implement recursive maximum finder
    def find_max(arr: List[int]) -> int:
        """
        Find the maximum element in a list using recursion.
        
        Args:
            arr: Non-empty list of integers
        
        Returns:
            Maximum element in the list
        
        Examples:
            find_max([3, 1, 4, 1, 5, 9]) -> 9
            find_max([42]) -> 42
            find_max([-1, -5, -3]) -> -1
        """
        # TODO: Implement recursive maximum finder
        pass
    
    # TODO: Implement recursive list flattening
    def flatten_list(nested_list: List[Any]) -> List[Any]:
        """
        Flatten a nested list using recursion.
        
        Args:
            nested_list: List that may contain sublists
        
        Returns:
            Flattened list with all elements at the same level
        
        Examples:
            flatten_list([1, [2, 3], [4, [5, 6]]]) -> [1, 2, 3, 4, 5, 6]
            flatten_list([1, 2, 3]) -> [1, 2, 3]
            flatten_list([]) -> []
        """
        # TODO: Implement recursive list flattening
        pass
    
    # TODO: Implement recursive binary search
    def binary_search(arr: List[int], target: int, left: int = 0, right: int = None) -> int:
        """
        Search for target in sorted array using recursive binary search.
        
        Args:
            arr: Sorted list of integers
            target: Value to search for
            left: Left boundary of search range
            right: Right boundary of search range
        
        Returns:
            Index of target if found, -1 otherwise
        
        Examples:
            binary_search([1, 3, 5, 7, 9], 5) -> 2
            binary_search([1, 3, 5, 7, 9], 6) -> -1
            binary_search([42], 42) -> 0
        """
        # TODO: Implement recursive binary search
        pass


# Exercise 3: Mathematical Recursion and Optimization
def exercise_3_mathematical_recursion():
    """
    Explore mathematical recursion and optimization techniques.
    """
    
    # TODO: Implement naive Fibonacci (for comparison)
    def fibonacci_naive(n: int) -> int:
        """
        Calculate nth Fibonacci number using naive recursion.
        This will be slow for large n - used for comparison.
        
        Args:
            n: Position in Fibonacci sequence (0-indexed)
        
        Returns:
            nth Fibonacci number
        
        Examples:
            fibonacci_naive(0) -> 0
            fibonacci_naive(1) -> 1
            fibonacci_naive(6) -> 8
        """
        # TODO: Implement naive recursive Fibonacci
        pass
    
    # TODO: Implement optimized Fibonacci with memoization
    def fibonacci_memoized(n: int, memo: dict = None) -> int:
        """
        Calculate nth Fibonacci number using memoization.
        Much faster than naive version for large n.
        
        Args:
            n: Position in Fibonacci sequence (0-indexed)
            memo: Dictionary to store computed values
        
        Returns:
            nth Fibonacci number
        
        Examples:
            fibonacci_memoized(0) -> 0
            fibonacci_memoized(1) -> 1
            fibonacci_memoized(50) -> 12586269025 (computes quickly)
        """
        # TODO: Implement memoized Fibonacci
        pass
    
    # TODO: Implement Towers of Hanoi
    def towers_of_hanoi(n: int, source: str, destination: str, auxiliary: str) -> List[str]:
        """
        Solve Towers of Hanoi puzzle and return list of moves.
        
        Args:
            n: Number of disks
            source: Name of source rod
            destination: Name of destination rod
            auxiliary: Name of auxiliary rod
        
        Returns:
            List of moves in format "Move disk from X to Y"
        
        Examples:
            towers_of_hanoi(2, "A", "C", "B") -> 
            ["Move disk from A to B", "Move disk from A to C", "Move disk from B to C"]
        """
        # TODO: Implement Towers of Hanoi solution
        pass
    
    # TODO: Implement recursive combination calculator
    def combinations(n: int, r: int) -> int:
        """
        Calculate C(n,r) = n! / (r! * (n-r)!) using recursion.
        Use the recursive formula: C(n,r) = C(n-1,r-1) + C(n-1,r)
        
        Args:
            n: Total number of items
            r: Number of items to choose
        
        Returns:
            Number of combinations
        
        Examples:
            combinations(5, 2) -> 10
            combinations(4, 0) -> 1
            combinations(6, 3) -> 20
        """
        # TODO: Implement recursive combinations
        pass


# Exercise 4: Tree Recursion
def exercise_4_tree_recursion():
    """
    Practice recursion with tree data structures.
    """
    
    class TreeNode:
        """Simple binary tree node."""
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    
    # TODO: Implement tree height calculation
    def tree_height(root: Optional[TreeNode]) -> int:
        """
        Calculate the height of a binary tree.
        
        Args:
            root: Root node of the tree
        
        Returns:
            Height of the tree (0 for empty tree)
        
        Examples:
            For tree:    1
                       /   \\
                      2     3
                     /
                    4
            tree_height(root) -> 3
        """
        # TODO: Implement recursive tree height calculation
        pass
    
    # TODO: Implement tree sum calculation
    def tree_sum(root: Optional[TreeNode]) -> int:
        """
        Calculate the sum of all values in a binary tree.
        
        Args:
            root: Root node of the tree
        
        Returns:
            Sum of all node values
        """
        # TODO: Implement recursive tree sum
        pass
    
    # TODO: Implement tree path sum checker
    def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
        """
        Check if there's a root-to-leaf path with given sum.
        
        Args:
            root: Root node of the tree
            target_sum: Target sum to find
        
        Returns:
            True if such path exists, False otherwise
        """
        # TODO: Implement recursive path sum checker
        pass
    
    # TODO: Implement tree mirroring
    def mirror_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Create a mirror image of the binary tree.
        
        Args:
            root: Root node of the tree
        
        Returns:
            Root of the mirrored tree
        """
        # TODO: Implement recursive tree mirroring
        pass


# Exercise 5: Backtracking
def exercise_5_backtracking():
    """
    Practice backtracking algorithms using recursion.
    """
    
    # TODO: Implement N-Queens solver
    def solve_n_queens(n: int) -> List[List[str]]:
        """
        Solve the N-Queens problem using backtracking.
        
        Args:
            n: Size of the chessboard (n x n)
        
        Returns:
            List of all possible solutions, where each solution is
            represented as a list of strings showing queen positions
        
        Examples:
            solve_n_queens(4) -> [
                [".Q..", "...Q", "Q...", "..Q."],
                ["..Q.", "Q...", "...Q", ".Q.."]
            ]
        """
        # TODO: Implement N-Queens backtracking solution
        pass
    
    # TODO: Implement subset generation
    def generate_subsets(nums: List[int]) -> List[List[int]]:
        """
        Generate all possible subsets of a list using backtracking.
        
        Args:
            nums: List of integers
        
        Returns:
            List of all subsets
        
        Examples:
            generate_subsets([1, 2, 3]) -> 
            [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
        """
        # TODO: Implement subset generation using backtracking
        pass
    
    # TODO: Implement permutation generation
    def generate_permutations(nums: List[int]) -> List[List[int]]:
        """
        Generate all permutations of a list using backtracking.
        
        Args:
            nums: List of integers
        
        Returns:
            List of all permutations
        
        Examples:
            generate_permutations([1, 2, 3]) -> 
            [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
        """
        # TODO: Implement permutation generation using backtracking
        pass
    
    # TODO: Implement maze solver
    def solve_maze(maze: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        Find a path through a maze using backtracking.
        
        Args:
            maze: 2D list where 0 = open path, 1 = wall
            start: Starting position (row, col)
            end: Ending position (row, col)
        
        Returns:
            List of coordinates representing the path, or empty list if no path
        
        Examples:
            maze = [[0, 1, 0], [0, 0, 0], [1, 0, 0]]
            solve_maze(maze, (0, 0), (2, 2)) -> [(0,0), (1,0), (1,1), (1,2), (2,2)]
        """
        # TODO: Implement maze solver using backtracking
        pass


# Performance Testing and Comparison
def performance_comparison():
    """
    Compare performance of different recursive approaches.
    """
    import time
    
    def time_function(func, *args):
        """Utility to time function execution."""
        start = time.time()
        result = func(*args)
        end = time.time()
        return result, end - start
    
    print("Recursion Performance Comparison")
    print("=" * 40)
    
    # Compare naive vs memoized Fibonacci
    print("Fibonacci Performance (n=30):")
    try:
        _, naive_time = time_function(fibonacci_naive, 30)
        print(f"Naive recursion: {naive_time:.4f} seconds")
    except:
        print("Naive Fibonacci not implemented")
    
    try:
        _, memo_time = time_function(fibonacci_memoized, 30)
        print(f"Memoized recursion: {memo_time:.4f} seconds")
        if 'naive_time' in locals():
            speedup = naive_time / memo_time if memo_time > 0 else float('inf')
            print(f"Speedup: {speedup:.0f}x faster")
    except:
        print("Memoized Fibonacci not implemented")


# Test Functions
def test_exercise_1():
    """Test basic recursion exercises."""
    print("Testing Exercise 1: Basic Recursion")
    
    try:
        assert power(2, 3) == 8
        assert power(5, 0) == 1
        assert power(3, 4) == 81
        print("✓ power function works correctly")
    except:
        print("✗ power function not working")
    
    try:
        assert sum_of_digits(123) == 6
        assert sum_of_digits(456) == 15
        assert sum_of_digits(0) == 0
        print("✓ sum_of_digits function works correctly")
    except:
        print("✗ sum_of_digits function not working")
    
    try:
        assert is_palindrome("racecar") == True
        assert is_palindrome("hello") == False
        assert is_palindrome("a") == True
        print("✓ is_palindrome function works correctly")
    except:
        print("✗ is_palindrome function not working")
    
    try:
        assert gcd(48, 18) == 6
        assert gcd(17, 13) == 1
        assert gcd(100, 25) == 25
        print("✓ gcd function works correctly")
    except:
        print("✗ gcd function not working")


def test_exercise_2():
    """Test list recursion exercises."""
    print("Testing Exercise 2: List Recursion")
    
    try:
        assert reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]
        assert reverse_list(['a', 'b', 'c']) == ['c', 'b', 'a']
        assert reverse_list([]) == []
        print("✓ reverse_list function works correctly")
    except:
        print("✗ reverse_list function not working")
    
    try:
        assert find_max([3, 1, 4, 1, 5, 9]) == 9
        assert find_max([42]) == 42
        assert find_max([-1, -5, -3]) == -1
        print("✓ find_max function works correctly")
    except:
        print("✗ find_max function not working")
    
    try:
        assert flatten_list([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]
        assert flatten_list([1, 2, 3]) == [1, 2, 3]
        assert flatten_list([]) == []
        print("✓ flatten_list function works correctly")
    except:
        print("✗ flatten_list function not working")
    
    try:
        assert binary_search([1, 3, 5, 7, 9], 5) == 2
        assert binary_search([1, 3, 5, 7, 9], 6) == -1
        assert binary_search([42], 42) == 0
        print("✓ binary_search function works correctly")
    except:
        print("✗ binary_search function not working")


def test_exercise_3():
    """Test mathematical recursion exercises."""
    print("Testing Exercise 3: Mathematical Recursion")
    
    try:
        assert fibonacci_naive(0) == 0
        assert fibonacci_naive(1) == 1
        assert fibonacci_naive(6) == 8
        print("✓ fibonacci_naive function works correctly")
    except:
        print("✗ fibonacci_naive function not working")
    
    try:
        assert fibonacci_memoized(0) == 0
        assert fibonacci_memoized(1) == 1
        assert fibonacci_memoized(6) == 8
        print("✓ fibonacci_memoized function works correctly")
    except:
        print("✗ fibonacci_memoized function not working")
    
    try:
        moves = towers_of_hanoi(2, "A", "C", "B")
        expected = ["Move disk from A to B", "Move disk from A to C", "Move disk from B to C"]
        assert moves == expected
        print("✓ towers_of_hanoi function works correctly")
    except:
        print("✗ towers_of_hanoi function not working")
    
    try:
        assert combinations(5, 2) == 10
        assert combinations(4, 0) == 1
        assert combinations(6, 3) == 20
        print("✓ combinations function works correctly")
    except:
        print("✗ combinations function not working")


def run_all_tests():
    """Run all test functions."""
    print("=" * 50)
    print("RECURSION EXERCISES - TEST RESULTS")
    print("=" * 50)
    
    test_exercise_1()
    print()
    test_exercise_2()
    print()
    test_exercise_3()
    print()
    
    print("=" * 50)
    print("Complete the TODO sections to pass all tests!")
    print("=" * 50)
    
    print()
    performance_comparison()


if __name__ == "__main__":
    run_all_tests()