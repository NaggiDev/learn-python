"""
Test file for Trees and Graphs exercises

This file contains comprehensive tests for the trees and graphs implementations.
Run this file to verify that your solutions are working correctly.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import importlib.util
import sys

# Load the solutions module
spec = importlib.util.spec_from_file_location("trees_graphs_solutions", 
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions", "04_trees_graphs.py"))
trees_graphs_solutions = importlib.util.module_from_spec(spec)
spec.loader.exec_module(trees_graphs_solutions)

# Import all classes and functions
TreeNode = trees_graphs_solutions.TreeNode
BinaryTree = trees_graphs_solutions.BinaryTree
BST = trees_graphs_solutions.BST
Graph = trees_graphs_solutions.Graph
tree_height = trees_graphs_solutions.tree_height
is_valid_bst = trees_graphs_solutions.is_valid_bst
lowest_common_ancestor = trees_graphs_solutions.lowest_common_ancestor
detect_cycle = trees_graphs_solutions.detect_cycle
shortest_path_unweighted = trees_graphs_solutions.shortest_path_unweighted
connected_components = trees_graphs_solutions.connected_components

def test_tree_node():
    """Test TreeNode class"""
    node = TreeNode(5)
    assert node.val == 5
    assert node.left is None
    assert node.right is None
    
    node.left = TreeNode(3)
    node.right = TreeNode(7)
    assert node.left.val == 3
    assert node.right.val == 7
    print("✓ TreeNode tests passed")

def test_binary_tree_comprehensive():
    """Comprehensive tests for Binary Tree"""
    bt = BinaryTree()
    
    # Test empty tree
    assert bt.level_order_traversal() == []
    assert bt.inorder_traversal() == []
    
    # Test single node
    bt.insert_level_order(1)
    assert bt.level_order_traversal() == [1]
    assert bt.inorder_traversal() == [1]
    
    # Test multiple nodes
    bt = BinaryTree()
    values = [1, 2, 3, 4, 5, 6, 7]
    for val in values:
        bt.insert_level_order(val)
    
    level_order = bt.level_order_traversal()
    inorder = bt.inorder_traversal()
    
    assert level_order == [1, 2, 3, 4, 5, 6, 7]
    assert inorder == [4, 2, 5, 1, 6, 3, 7]
    
    print("✓ Binary Tree comprehensive tests passed")

def test_bst_comprehensive():
    """Comprehensive tests for Binary Search Tree"""
    bst = BST()
    
    # Test empty BST
    assert bst.search(5) == False
    assert bst.find_min() is None
    assert bst.find_max() is None
    
    # Test single node
    bst.insert(5)
    assert bst.search(5) == True
    assert bst.search(3) == False
    assert bst.find_min() == 5
    assert bst.find_max() == 5
    
    # Test multiple nodes
    values = [3, 7, 2, 4, 6, 8, 1, 9]
    for val in values:
        bst.insert(val)
    
    # Test search
    for val in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        assert bst.search(val) == True
    
    assert bst.search(0) == False
    assert bst.search(10) == False
    
    # Test min/max
    assert bst.find_min() == 1
    assert bst.find_max() == 9
    
    print("✓ BST comprehensive tests passed")

def test_graph_comprehensive():
    """Comprehensive tests for Graph"""
    g = Graph()
    
    # Test empty graph
    assert g.get_vertices() == []
    assert g.get_neighbors('A') == []
    
    # Test single vertex
    g.add_vertex('A')
    assert 'A' in g.get_vertices()
    assert g.get_neighbors('A') == []
    
    # Test edges
    g.add_edge('A', 'B')
    vertices = g.get_vertices()
    assert 'A' in vertices and 'B' in vertices
    assert 'B' in g.get_neighbors('A')
    assert 'A' in g.get_neighbors('B')  # Undirected by default
    
    # Test directed edge
    g2 = Graph()
    g2.add_edge('X', 'Y', directed=True)
    assert 'Y' in g2.get_neighbors('X')
    assert 'X' not in g2.get_neighbors('Y')
    
    # Test complex graph
    g3 = Graph()
    edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('A', 'C'), ('D', 'E')]
    for v1, v2 in edges:
        g3.add_edge(v1, v2)
    
    # Test DFS
    dfs_result = g3.dfs('A')
    assert len(dfs_result) == 5
    assert dfs_result[0] == 'A'
    assert set(dfs_result) == {'A', 'B', 'C', 'D', 'E'}
    
    # Test BFS
    bfs_result = g3.bfs('A')
    assert len(bfs_result) == 5
    assert bfs_result[0] == 'A'
    assert set(bfs_result) == {'A', 'B', 'C', 'D', 'E'}
    
    # Test path finding
    assert g3.has_path('A', 'E') == True
    assert g3.has_path('A', 'F') == False
    assert g3.has_path('A', 'A') == True
    
    print("✓ Graph comprehensive tests passed")

def test_tree_algorithms_comprehensive():
    """Comprehensive tests for tree algorithms"""
    
    # Test tree_height
    assert tree_height(None) == -1
    
    single_node = TreeNode(1)
    assert tree_height(single_node) == 0
    
    # Balanced tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    assert tree_height(root) == 2
    
    # Unbalanced tree
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    assert tree_height(root2) == 3
    
    # Test is_valid_bst
    assert is_valid_bst(None) == True
    assert is_valid_bst(single_node) == True
    
    # Valid BST
    bst_root = TreeNode(5)
    bst_root.left = TreeNode(3)
    bst_root.right = TreeNode(7)
    bst_root.left.left = TreeNode(2)
    bst_root.left.right = TreeNode(4)
    bst_root.right.left = TreeNode(6)
    bst_root.right.right = TreeNode(8)
    assert is_valid_bst(bst_root) == True
    
    # Invalid BST
    invalid_bst = TreeNode(5)
    invalid_bst.left = TreeNode(3)
    invalid_bst.right = TreeNode(7)
    invalid_bst.left.right = TreeNode(6)  # This violates BST property
    assert is_valid_bst(invalid_bst) == False
    
    # Test LCA
    assert lowest_common_ancestor(bst_root, 2, 4) == 3
    assert lowest_common_ancestor(bst_root, 6, 8) == 7
    assert lowest_common_ancestor(bst_root, 2, 8) == 5
    assert lowest_common_ancestor(bst_root, 3, 4) == 3
    
    print("✓ Tree algorithms comprehensive tests passed")

def test_graph_algorithms_comprehensive():
    """Comprehensive tests for graph algorithms"""
    
    # Test cycle detection
    # Graph without cycle
    g1 = Graph()
    g1.add_edge('A', 'B')
    g1.add_edge('B', 'C')
    g1.add_edge('C', 'D')
    assert detect_cycle(g1) == False
    
    # Graph with cycle
    g2 = Graph()
    g2.add_edge('A', 'B')
    g2.add_edge('B', 'C')
    g2.add_edge('C', 'A')
    assert detect_cycle(g2) == True
    
    # Test shortest path
    g3 = Graph()
    g3.add_edge('A', 'B')
    g3.add_edge('B', 'C')
    g3.add_edge('C', 'D')
    g3.add_edge('A', 'D')  # Direct path
    
    path_long = shortest_path_unweighted(g3, 'A', 'C')
    path_short = shortest_path_unweighted(g3, 'A', 'D')
    
    assert len(path_long) == 3  # A -> B -> C
    assert path_long[0] == 'A' and path_long[-1] == 'C'
    assert len(path_short) == 2  # A -> D
    assert path_short == ['A', 'D']
    
    # No path
    g4 = Graph()
    g4.add_edge('A', 'B')
    g4.add_edge('C', 'D')
    assert shortest_path_unweighted(g4, 'A', 'C') == []
    
    # Test connected components
    g5 = Graph()
    g5.add_edge('A', 'B')
    g5.add_edge('B', 'C')
    g5.add_edge('D', 'E')
    g5.add_vertex('F')  # Isolated vertex
    
    components = connected_components(g5)
    assert len(components) == 3
    
    # Sort components by size for consistent testing
    components.sort(key=len, reverse=True)
    assert len(components[0]) == 3  # {A, B, C}
    assert len(components[1]) == 2  # {D, E}
    assert len(components[2]) == 1  # {F}
    
    print("✓ Graph algorithms comprehensive tests passed")

def test_edge_cases():
    """Test edge cases and error conditions"""
    
    # Empty inputs
    assert tree_height(None) == -1
    assert is_valid_bst(None) == True
    
    # Graph with self-loops (if supported)
    g = Graph()
    g.add_edge('A', 'A')
    assert 'A' in g.get_neighbors('A')
    
    # Single node graph
    g2 = Graph()
    g2.add_vertex('X')
    assert g2.dfs('X') == ['X']
    assert g2.bfs('X') == ['X']
    assert g2.has_path('X', 'X') == True
    
    print("✓ Edge cases tests passed")

def run_all_tests():
    """Run all test functions"""
    print("Running comprehensive tests for Trees and Graphs...")
    print("=" * 60)
    
    test_tree_node()
    test_binary_tree_comprehensive()
    test_bst_comprehensive()
    test_graph_comprehensive()
    test_tree_algorithms_comprehensive()
    test_graph_algorithms_comprehensive()
    test_edge_cases()
    
    print("\n🎉 All comprehensive tests passed!")
    print("Your trees and graphs implementations are working correctly.")

if __name__ == "__main__":
    run_all_tests()