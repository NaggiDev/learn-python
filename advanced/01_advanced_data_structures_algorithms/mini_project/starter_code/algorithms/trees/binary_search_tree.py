"""
Binary Search Tree Implementation

This module implements a Binary Search Tree (BST) with standard operations
including insert, delete, search, and various traversals.

BST Properties:
- Left subtree contains only nodes with values less than parent
- Right subtree contains only nodes with values greater than parent
- Both left and right subtrees are also BSTs
"""

from typing import Optional, List, TypeVar, Generic
from dataclasses import dataclass

T = TypeVar('T')


@dataclass
class TreeNode(Generic[T]):
    """Node class for Binary Search Tree."""
    value: T
    left: Optional['TreeNode[T]'] = None
    right: Optional['TreeNode[T]'] = None


class BinarySearchTree(Generic[T]):
    """
    Binary Search Tree implementation with standard operations.
    
    Time Complexities (average case):
    - Insert: O(log n)
    - Delete: O(log n)
    - Search: O(log n)
    - Traversal: O(n)
    
    Worst case (unbalanced tree): O(n) for all operations
    """
    
    def __init__(self):
        """Initialize an empty BST."""
        self.root: Optional[TreeNode[T]] = None
        self.size = 0
    
    def insert(self, value: T) -> None:
        """
        Insert a value into the BST.
        
        Args:
            value: Value to insert
            
        Time Complexity: O(log n) average, O(n) worst case
        """
        # TODO: Implement insert operation
        # Use helper method for recursive insertion
        pass
    
    def _insert_recursive(self, node: Optional[TreeNode[T]], value: T) -> TreeNode[T]:
        """
        Recursive helper method for insertion.
        
        Args:
            node: Current node in recursion
            value: Value to insert
            
        Returns:
            Root of the subtree after insertion
        """
        # TODO: Implement recursive insertion
        # Base case: create new node if current node is None
        # Recursive case: go left or right based on value comparison
        pass
    
    def search(self, value: T) -> bool:
        """
        Search for a value in the BST.
        
        Args:
            value: Value to search for
            
        Returns:
            True if value exists, False otherwise
            
        Time Complexity: O(log n) average, O(n) worst case
        """
        # TODO: Implement search operation
        pass
    
    def _search_recursive(self, node: Optional[TreeNode[T]], value: T) -> bool:
        """
        Recursive helper method for search.
        
        Args:
            node: Current node in recursion
            value: Value to search for
            
        Returns:
            True if value found, False otherwise
        """
        # TODO: Implement recursive search
        pass
    
    def delete(self, value: T) -> bool:
        """
        Delete a value from the BST.
        
        Args:
            value: Value to delete
            
        Returns:
            True if value was deleted, False if not found
            
        Time Complexity: O(log n) average, O(n) worst case
        """
        # TODO: Implement delete operation
        # Handle three cases: no children, one child, two children
        pass
    
    def _delete_recursive(self, node: Optional[TreeNode[T]], value: T) -> Optional[TreeNode[T]]:
        """
        Recursive helper method for deletion.
        
        Args:
            node: Current node in recursion
            value: Value to delete
            
        Returns:
            Root of the subtree after deletion
        """
        # TODO: Implement recursive deletion
        # Handle three cases for node deletion
        pass
    
    def _find_min(self, node: TreeNode[T]) -> TreeNode[T]:
        """
        Find the minimum value node in a subtree.
        
        Args:
            node: Root of subtree
            
        Returns:
            Node with minimum value
        """
        # TODO: Find leftmost node (minimum value)
        pass
    
    def inorder_traversal(self) -> List[T]:
        """
        Perform inorder traversal of the BST.
        
        Returns:
            List of values in sorted order
            
        Time Complexity: O(n)
        """
        # TODO: Implement inorder traversal (left, root, right)
        # This should return values in sorted order for a BST
        pass
    
    def preorder_traversal(self) -> List[T]:
        """
        Perform preorder traversal of the BST.
        
        Returns:
            List of values in preorder
            
        Time Complexity: O(n)
        """
        # TODO: Implement preorder traversal (root, left, right)
        pass
    
    def postorder_traversal(self) -> List[T]:
        """
        Perform postorder traversal of the BST.
        
        Returns:
            List of values in postorder
            
        Time Complexity: O(n)
        """
        # TODO: Implement postorder traversal (left, right, root)
        pass
    
    def height(self) -> int:
        """
        Calculate the height of the BST.
        
        Returns:
            Height of the tree (0 for empty tree)
            
        Time Complexity: O(n)
        """
        # TODO: Calculate tree height recursively
        pass
    
    def _height_recursive(self, node: Optional[TreeNode[T]]) -> int:
        """
        Recursive helper method for height calculation.
        
        Args:
            node: Current node
            
        Returns:
            Height of subtree rooted at node
        """
        # TODO: Calculate height recursively
        pass
    
    def is_balanced(self) -> bool:
        """
        Check if the BST is balanced.
        A tree is balanced if the height difference between left and right
        subtrees is at most 1 for all nodes.
        
        Returns:
            True if tree is balanced, False otherwise
            
        Time Complexity: O(n)
        """
        # TODO: Check if tree is balanced
        pass
    
    def _is_balanced_recursive(self, node: Optional[TreeNode[T]]) -> tuple[bool, int]:
        """
        Recursive helper for balance checking.
        
        Args:
            node: Current node
            
        Returns:
            Tuple of (is_balanced, height)
        """
        # TODO: Check balance and calculate height simultaneously
        pass
    
    def __len__(self) -> int:
        """Return the number of nodes in the BST."""
        return self.size
    
    def __bool__(self) -> bool:
        """Return True if BST is not empty."""
        return self.root is not None
    
    def __str__(self) -> str:
        """Return string representation of BST."""
        if not self.root:
            return "Empty BST"
        return f"BST with {self.size} nodes: {self.inorder_traversal()}"