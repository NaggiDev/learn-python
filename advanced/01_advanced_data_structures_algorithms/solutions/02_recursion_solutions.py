"""
Recursion Exercises - Solutions

This file contains complete solutions to all recursion exercises
with detailed explanations and complexity analysis.
"""

from typing import List, Optional, Tuple, Any


# Exercise 1: Basic Recursion - SOLUTIONS
def exercise_1_basic_recursion():
    """
    Solutions for basic recursive functions.
    """
    
    def power(base: int, exponent: int) -> int:
        """
        Calculate base^exponent using recursion.
        Time Complexity: O(exponent)
        Space Complexity: O(exponent) due to recursion stack
        """
        # Base case: any number to the power of 0 is 1
        if exponent == 0:
            return 1
        
        # Recursive case: base^n = base * base^(n-1)
        return base * power(base, exponent - 1)
    
    def sum_of_digits(n: int) -> int:
        """
        Calculate the sum of digits in a number using recursion.
        Time Complexity: O(log n) - number of digits
        Space Complexity: O(log n) due to recursion stack
        """
        # Base case: single digit number
        if n < 10:
            return n
        
        # Recursive case: last digit + sum of remaining digits
        return (n % 10) + sum_of_digits(n // 10)
    
    def is_palindrome(s: str) -> bool:
        """
        Check if a string is a palindrome using recursion.
        Time Complexity: O(n)
        Space Complexity: O(n) due to recursion stack
        """
        # Base cases: empty string or single character
        if len(s) <= 1:
            return True
        
        # Check first and last characters, then recurse on middle
        if s[0] != s[-1]:
            return False
        
        return is_palindrome(s[1:-1])
    
    def gcd(a: int, b: int) -> int:
        """
        Find the greatest common divisor using Euclidean algorithm (recursive).
        Time Complexity: O(log(min(a, b)))
        Space Complexity: O(log(min(a, b))) due to recursion stack
        """
        # Base case: when b is 0, GCD is a
        if b == 0:
            return a
        
        # Recursive case: GCD(a, b) = GCD(b, a mod b)
        return gcd(b, a % b)


# Exercise 2: List and Array Recursion - SOLUTIONS
def exercise_2_list_recursion():
    """
    Solutions for list recursion exercises.
    """
    
    def reverse_list(arr: List[Any]) -> List[Any]:
        """
        Reverse a list using recursion.
        Time Complexity: O(n)
        Space Complexity: O(n) for result + O(n) for recursion stack
        """
        # Base case: empty list or single element
        if len(arr) <= 1:
            return arr[:]
        
        # Recursive case: last element + reversed rest
        return [arr[-1]] + reverse_list(arr[:-1])
    
    def find_max(arr: List[int]) -> int:
        """
        Find the maximum element in a list using recursion.
        Time Complexity: O(n)
        Space Complexity: O(n) due to recursion stack
        """
        # Base case: single element
        if len(arr) == 1:
            return arr[0]
        
        # Recursive case: max of first element and max of rest
        max_of_rest = find_max(arr[1:])
        return max(arr[0], max_of_rest)
    
    def flatten_list(nested_list: List[Any]) -> List[Any]:
        """
        Flatten a nested list using recursion.
        Time Complexity: O(n) where n is total number of elements
        Space Complexity: O(d) where d is maximum nesting depth
        """
        result = []
        
        for item in nested_list:
            if isinstance(item, list):
                # Recursive case: flatten the sublist
                result.extend(flatten_list(item))
            else:
                # Base case: regular element
                result.append(item)
        
        return result
    
    def binary_search(arr: List[int], target: int, left: int = 0, right: int = None) -> int:
        """
        Search for target in sorted array using recursive binary search.
        Time Complexity: O(log n)
        Space Complexity: O(log n) due to recursion stack
        """
        if right is None:
            right = len(arr) - 1
        
        # Base case: search space is empty
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        # Base case: found the target
        if arr[mid] == target:
            return mid
        
        # Recursive cases: search left or right half
        if arr[mid] > target:
            return binary_search(arr, target, left, mid - 1)
        else:
            return binary_search(arr, target, mid + 1, right)


# Exercise 3: Mathematical Recursion and Optimization - SOLUTIONS
def exercise_3_mathematical_recursion():
    """
    Solutions for mathematical recursion exercises.
    """
    
    def fibonacci_naive(n: int) -> int:
        """
        Calculate nth Fibonacci number using naive recursion.
        Time Complexity: O(2^n) - exponential!
        Space Complexity: O(n) due to maximum recursion depth
        """
        # Base cases
        if n <= 1:
            return n
        
        # Recursive case: F(n) = F(n-1) + F(n-2)
        return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)
    
    def fibonacci_memoized(n: int, memo: dict = None) -> int:
        """
        Calculate nth Fibonacci number using memoization.
        Time Complexity: O(n) - each number calculated once
        Space Complexity: O(n) for memo dict + O(n) for recursion stack
        """
        if memo is None:
            memo = {}
        
        # Check if already computed
        if n in memo:
            return memo[n]
        
        # Base cases
        if n <= 1:
            return n
        
        # Compute and store result
        memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
        return memo[n]
    
    def towers_of_hanoi(n: int, source: str, destination: str, auxiliary: str) -> List[str]:
        """
        Solve Towers of Hanoi puzzle and return list of moves.
        Time Complexity: O(2^n)
        Space Complexity: O(n) for recursion stack + O(2^n) for result list
        """
        if n == 1:
            # Base case: move single disk directly
            return [f"Move disk from {source} to {destination}"]
        
        moves = []
        
        # Step 1: Move n-1 disks from source to auxiliary
        moves.extend(towers_of_hanoi(n - 1, source, auxiliary, destination))
        
        # Step 2: Move the largest disk from source to destination
        moves.append(f"Move disk from {source} to {destination}")
        
        # Step 3: Move n-1 disks from auxiliary to destination
        moves.extend(towers_of_hanoi(n - 1, auxiliary, destination, source))
        
        return moves
    
    def combinations(n: int, r: int) -> int:
        """
        Calculate C(n,r) using Pascal's triangle recursion.
        Time Complexity: O(2^min(r, n-r)) without memoization
        Space Complexity: O(min(r, n-r)) for recursion depth
        """
        # Base cases
        if r == 0 or r == n:
            return 1
        if r > n:
            return 0
        
        # Recursive case: C(n,r) = C(n-1,r-1) + C(n-1,r)
        return combinations(n - 1, r - 1) + combinations(n - 1, r)


# Exercise 4: Tree Recursion - SOLUTIONS
def exercise_4_tree_recursion():
    """
    Solutions for tree recursion exercises.
    """
    
    class TreeNode:
        """Simple binary tree node."""
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    
    def tree_height(root: Optional[TreeNode]) -> int:
        """
        Calculate the height of a binary tree.
        Time Complexity: O(n) where n is number of nodes
        Space Complexity: O(h) where h is height of tree
        """
        # Base case: empty tree
        if not root:
            return 0
        
        # Recursive case: 1 + max height of subtrees
        left_height = tree_height(root.left)
        right_height = tree_height(root.right)
        
        return 1 + max(left_height, right_height)
    
    def tree_sum(root: Optional[TreeNode]) -> int:
        """
        Calculate the sum of all values in a binary tree.
        Time Complexity: O(n)
        Space Complexity: O(h) for recursion stack
        """
        # Base case: empty tree
        if not root:
            return 0
        
        # Recursive case: current value + sum of subtrees
        return root.val + tree_sum(root.left) + tree_sum(root.right)
    
    def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
        """
        Check if there's a root-to-leaf path with given sum.
        Time Complexity: O(n) in worst case
        Space Complexity: O(h) for recursion stack
        """
        # Base case: empty tree
        if not root:
            return False
        
        # Base case: leaf node
        if not root.left and not root.right:
            return root.val == target_sum
        
        # Recursive case: check both subtrees with reduced target
        remaining_sum = target_sum - root.val
        return (has_path_sum(root.left, remaining_sum) or 
                has_path_sum(root.right, remaining_sum))
    
    def mirror_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Create a mirror image of the binary tree.
        Time Complexity: O(n)
        Space Complexity: O(h) for recursion stack
        """
        # Base case: empty tree
        if not root:
            return None
        
        # Create new node with mirrored children
        mirrored = TreeNode(root.val)
        mirrored.left = mirror_tree(root.right)   # Left becomes right
        mirrored.right = mirror_tree(root.left)   # Right becomes left
        
        return mirrored


# Exercise 5: Backtracking - SOLUTIONS
def exercise_5_backtracking():
    """
    Solutions for backtracking exercises.
    """
    
    def solve_n_queens(n: int) -> List[List[str]]:
        """
        Solve the N-Queens problem using backtracking.
        Time Complexity: O(n!) in worst case
        Space Complexity: O(n) for recursion stack and board state
        """
        def is_safe(board, row, col):
            """Check if placing queen at (row, col) is safe."""
            # Check column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            # Check diagonal (top-left to bottom-right)
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            # Check diagonal (top-right to bottom-left)
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            
            return True
        
        def backtrack(board, row):
            """Recursively place queens using backtracking."""
            # Base case: all queens placed
            if row == n:
                result.append([''.join(row) for row in board])
                return
            
            # Try placing queen in each column of current row
            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(board, row + 1)
                    board[row][col] = '.'  # Backtrack
        
        result = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(board, 0)
        return result
    
    def generate_subsets(nums: List[int]) -> List[List[int]]:
        """
        Generate all possible subsets using backtracking.
        Time Complexity: O(2^n) - there are 2^n subsets
        Space Complexity: O(n) for recursion stack
        """
        def backtrack(start, current_subset):
            # Add current subset to result
            result.append(current_subset[:])
            
            # Try adding each remaining element
            for i in range(start, len(nums)):
                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()  # Backtrack
        
        result = []
        backtrack(0, [])
        return result
    
    def generate_permutations(nums: List[int]) -> List[List[int]]:
        """
        Generate all permutations using backtracking.
        Time Complexity: O(n! * n) - n! permutations, each takes O(n) to create
        Space Complexity: O(n) for recursion stack
        """
        def backtrack(current_permutation):
            # Base case: permutation is complete
            if len(current_permutation) == len(nums):
                result.append(current_permutation[:])
                return
            
            # Try each unused number
            for num in nums:
                if num not in current_permutation:
                    current_permutation.append(num)
                    backtrack(current_permutation)
                    current_permutation.pop()  # Backtrack
        
        result = []
        backtrack([])
        return result
    
    def solve_maze(maze: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        Find a path through a maze using backtracking.
        Time Complexity: O(4^(m*n)) in worst case
        Space Complexity: O(m*n) for recursion stack and visited set
        """
        def is_valid(row, col, visited):
            """Check if position is valid and unvisited."""
            return (0 <= row < len(maze) and 
                    0 <= col < len(maze[0]) and 
                    maze[row][col] == 0 and 
                    (row, col) not in visited)
        
        def backtrack(row, col, path, visited):
            """Recursively find path using backtracking."""
            # Base case: reached destination
            if (row, col) == end:
                return True
            
            # Try all four directions
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if is_valid(new_row, new_col, visited):
                    path.append((new_row, new_col))
                    visited.add((new_row, new_col))
                    
                    if backtrack(new_row, new_col, path, visited):
                        return True
                    
                    # Backtrack
                    path.pop()
                    visited.remove((new_row, new_col))
            
            return False
        
        # Initialize path and visited set
        path = [start]
        visited = {start}
        
        # Start backtracking from start position
        if backtrack(start[0], start[1], path, visited):
            return path
        else:
            return []


# Performance Testing and Demonstration
def demonstrate_recursion_optimization():
    """
    Demonstrate the impact of recursion optimization techniques.
    """
    import time
    
    print("Recursion Optimization Demonstration")
    print("=" * 50)
    
    # Compare naive vs memoized Fibonacci
    print("Fibonacci Performance Comparison:")
    print("-" * 30)
    
    test_values = [20, 25, 30, 35]
    
    for n in test_values:
        # Memoized version (always fast)
        start_time = time.time()
        result_memo = fibonacci_memoized(n)
        memo_time = time.time() - start_time
        
        # Naive version (only for smaller values to avoid long waits)
        if n <= 30:
            start_time = time.time()
            result_naive = fibonacci_naive(n)
            naive_time = time.time() - start_time
            
            speedup = naive_time / memo_time if memo_time > 0 else float('inf')
            print(f"n={n}: Naive={naive_time:.4f}s, Memoized={memo_time:.6f}s, Speedup={speedup:.0f}x")
        else:
            print(f"n={n}: Naive=too slow!, Memoized={memo_time:.6f}s")
    
    print("\nTowers of Hanoi Complexity:")
    print("-" * 30)
    
    for n in [3, 4, 5, 6]:
        start_time = time.time()
        moves = towers_of_hanoi(n, "A", "C", "B")
        elapsed_time = time.time() - start_time
        
        print(f"n={n}: {len(moves)} moves, {elapsed_time:.6f}s")


# Comprehensive Testing
def test_all_solutions():
    """Test all solution implementations."""
    print("Testing All Recursion Solutions")
    print("=" * 50)
    
    # Test Exercise 1
    print("Exercise 1: Basic Recursion")
    assert power(2, 3) == 8
    assert sum_of_digits(123) == 6
    assert is_palindrome("racecar") == True
    assert gcd(48, 18) == 6
    print("✓ All basic recursion functions work correctly")
    
    # Test Exercise 2
    print("\nExercise 2: List Recursion")
    assert reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert find_max([3, 1, 4, 1, 5, 9]) == 9
    assert flatten_list([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]
    assert binary_search([1, 3, 5, 7, 9], 5) == 2
    print("✓ All list recursion functions work correctly")
    
    # Test Exercise 3
    print("\nExercise 3: Mathematical Recursion")
    assert fibonacci_naive(6) == 8
    assert fibonacci_memoized(6) == 8
    moves = towers_of_hanoi(2, "A", "C", "B")
    assert len(moves) == 3
    assert combinations(5, 2) == 10
    print("✓ All mathematical recursion functions work correctly")
    
    # Test Exercise 4
    print("\nExercise 4: Tree Recursion")
    from exercise_4_tree_recursion import TreeNode
    
    # Create test tree:    1
    #                    /   \
    #                   2     3
    #                  /
    #                 4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    
    assert tree_height(root) == 3
    assert tree_sum(root) == 10
    assert has_path_sum(root, 7) == True  # 1 + 2 + 4 = 7
    print("✓ All tree recursion functions work correctly")
    
    # Test Exercise 5
    print("\nExercise 5: Backtracking")
    queens_solutions = solve_n_queens(4)
    assert len(queens_solutions) == 2
    
    subsets = generate_subsets([1, 2])
    assert len(subsets) == 4  # [], [1], [2], [1,2]
    
    perms = generate_permutations([1, 2])
    assert len(perms) == 2  # [1,2], [2,1]
    
    # Test maze solver
    maze = [[0, 1, 0], [0, 0, 0], [1, 0, 0]]
    path = solve_maze(maze, (0, 0), (2, 2))
    assert len(path) > 0  # Should find a path
    print("✓ All backtracking functions work correctly")
    
    print("\n" + "=" * 50)
    print("ALL TESTS PASSED! 🎉")
    print("=" * 50)


if __name__ == "__main__":
    test_all_solutions()
    print()
    demonstrate_recursion_optimization()