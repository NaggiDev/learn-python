"""
AVL Tree Implementation

This module implements an AVL Tree, which is a self-balancing Binary Search Tree.
In an AVL tree, the heights of the two child subtrees of any node differ by at most one.

AVL Tree Properties:
- All BST properties apply
- Height difference between left and right subtrees is at most 1
- Automatically rebalances after insertions and deletions
"""

from typing import Optional, List, TypeVar, Generic
from dataclasses import dataclass

T = TypeVar('T')


@dataclass
class AVLNode(Generic[T]):
    """Node class for AVL Tree with height tracking."""
    value: T
    left: Optional['AVLNode[T]'] = None
    right: Optional['AVLNode[T]'] = None
    height: int = 1


class AVLTree(Generic[T]):
    """
    AVL Tree implementation with automatic balancing.
    
    Time Complexities (guaranteed):
    - Insert: O(log n)
    - Delete: O(log n)
    - Search: O(log n)
    - All operations are guaranteed O(log n) due to balancing
    """
    
    def __init__(self):
        """Initialize an empty AVL Tree."""
        self.root: Optional[AVLNode[T]] = None
        self.size = 0
    
    def insert(self, value: T) -> None:
        """
        Insert a value into the AVL Tree.
        
        Args:
            value: Value to insert
            
        Time Complexity: O(log n)
        """
        # TODO: Implement insert with automatic balancing
        pass
    
    def _insert_recursive(self, node: Optional[AVLNode[T]], value: T) -> AVLNode[T]:
        """
        Recursive helper method for insertion with balancing.
        
        Args:
            node: Current node in recursion
            value: Value to insert
            
        Returns:
            Root of the balanced subtree after insertion
        """
        # TODO: Implement recursive insertion with balancing
        # 1. Perform normal BST insertion
        # 2. Update height of current node
        # 3. Check balance factor and perform rotations if needed
        pass
    
    def delete(self, value: T) -> bool:
        """
        Delete a value from the AVL Tree.
        
        Args:
            value: Value to delete
            
        Returns:
            True if value was deleted, False if not found
            
        Time Complexity: O(log n)
        """
        # TODO: Implement delete with automatic balancing
        pass
    
    def _delete_recursive(self, node: Optional[AVLNode[T]], value: T) -> Optional[AVLNode[T]]:
        """
        Recursive helper method for deletion with balancing.
        
        Args:
            node: Current node in recursion
            value: Value to delete
            
        Returns:
            Root of the balanced subtree after deletion
        """
        # TODO: Implement recursive deletion with balancing
        # 1. Perform normal BST deletion
        # 2. Update height of current node
        # 3. Check balance factor and perform rotations if needed
        pass
    
    def search(self, value: T) -> bool:
        """
        Search for a value in the AVL Tree.
        
        Args:
            value: Value to search for
            
        Returns:
            True if value exists, False otherwise
            
        Time Complexity: O(log n)
        """
        # TODO: Implement search (same as BST)
        pass
    
    def _get_height(self, node: Optional[AVLNode[T]]) -> int:
        """
        Get the height of a node.
        
        Args:
            node: Node to get height of
            
        Returns:
            Height of the node (0 for None)
        """
        # TODO: Return node height or 0 if node is None
        pass
    
    def _update_height(self, node: AVLNode[T]) -> None:
        """
        Update the height of a node based on its children.
        
        Args:
            node: Node to update height for
        """
        # TODO: Update node height based on children heights
        pass
    
    def _get_balance_factor(self, node: AVLNode[T]) -> int:
        """
        Calculate the balance factor of a node.
        Balance factor = height(left) - height(right)
        
        Args:
            node: Node to calculate balance factor for
            
        Returns:
            Balance factor (-2 to 2 for valid AVL tree)
        """
        # TODO: Calculate and return balance factor
        pass
    
    def _rotate_right(self, y: AVLNode[T]) -> AVLNode[T]:
        """
        Perform right rotation.
        
        Args:
            y: Root of subtree to rotate
            
        Returns:
            New root after rotation
        """
        # TODO: Implement right rotation
        # Used to fix left-heavy imbalance
        pass
    
    def _rotate_left(self, x: AVLNode[T]) -> AVLNode[T]:
        """
        Perform left rotation.
        
        Args:
            x: Root of subtree to rotate
            
        Returns:
            New root after rotation
        """
        # TODO: Implement left rotation
        # Used to fix right-heavy imbalance
        pass
    
    def _find_min(self, node: AVLNode[T]) -> AVLNode[T]:
        """
        Find the minimum value node in a subtree.
        
        Args:
            node: Root of subtree
            
        Returns:
            Node with minimum value
        """
        # TODO: Find leftmost node
        pass
    
    def inorder_traversal(self) -> List[T]:
        """
        Perform inorder traversal of the AVL Tree.
        
        Returns:
            List of values in sorted order
            
        Time Complexity: O(n)
        """
        # TODO: Implement inorder traversal
        pass
    
    def _inorder_recursive(self, node: Optional[AVLNode[T]], result: List[T]) -> None:
        """
        Recursive helper for inorder traversal.
        
        Args:
            node: Current node
            result: List to store traversal result
        """
        # TODO: Implement recursive inorder traversal
        pass
    
    def is_balanced(self) -> bool:
        """
        Check if the tree satisfies AVL property.
        
        Returns:
            True if tree is properly balanced (should always be True for AVL tree)
            
        Time Complexity: O(n)
        """
        # TODO: Verify AVL property for all nodes
        pass
    
    def _is_balanced_recursive(self, node: Optional[AVLNode[T]]) -> bool:
        """
        Recursive helper for balance verification.
        
        Args:
            node: Current node
            
        Returns:
            True if subtree is balanced
        """
        # TODO: Check AVL property recursively
        pass
    
    def get_height(self) -> int:
        """
        Get the height of the AVL Tree.
        
        Returns:
            Height of the tree
        """
        return self._get_height(self.root)
    
    def __len__(self) -> int:
        """Return the number of nodes in the AVL Tree."""
        return self.size
    
    def __bool__(self) -> bool:
        """Return True if AVL Tree is not empty."""
        return self.root is not None
    
    def __str__(self) -> str:
        """Return string representation of AVL Tree."""
        if not self.root:
            return "Empty AVL Tree"
        return f"AVL Tree with {self.size} nodes (height: {self.get_height()}): {self.inorder_traversal()}"