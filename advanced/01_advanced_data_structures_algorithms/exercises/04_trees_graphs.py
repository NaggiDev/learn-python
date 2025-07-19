"""
Trees and Graphs Exercises

This file contains exercises to practice implementing and working with tree and graph data structures.
Complete each function according to the instructions and run the tests to verify your solutions.
"""

# Exercise 1: Binary Tree Implementation
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert_level_order(self, val):
        """
        Insert a value into the binary tree using level-order insertion.
        
        TODO: Implement level-order insertion
        - If tree is empty, create root
        - Otherwise, find the first node with an empty child slot
        - Insert the new node there
        """
        # TODO: Implement this method
        pass
    
    def inorder_traversal(self):
        """
        Perform inorder traversal of the binary tree.
        
        TODO: Implement inorder traversal (Left -> Root -> Right)
        Return a list of values in inorder sequence
        """
        # TODO: Implement this method
        pass
    
    def level_order_traversal(self):
        """
        Perform level-order traversal of the binary tree.
        
        TODO: Implement level-order traversal using a queue
        Return a list of values in level-order sequence
        """
        # TODO: Implement this method
        pass

# Exercise 2: Binary Search Tree Implementation
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        """
        Insert a value into the BST maintaining BST property.
        
        TODO: Implement BST insertion
        - Values less than current node go to left subtree
        - Values greater than current node go to right subtree
        - Duplicate values can be ignored or handled as preferred
        """
        # TODO: Implement this method
        pass
    
    def search(self, val):
        """
        Search for a value in the BST.
        
        TODO: Implement BST search
        Return True if value exists, False otherwise
        """
        # TODO: Implement this method
        pass
    
    def find_min(self):
        """
        Find the minimum value in the BST.
        
        TODO: Implement finding minimum value
        The minimum value is the leftmost node
        """
        # TODO: Implement this method
        pass
    
    def find_max(self):
        """
        Find the maximum value in the BST.
        
        TODO: Implement finding maximum value
        The maximum value is the rightmost node
        """
        # TODO: Implement this method
        pass

# Exercise 3: Graph Implementation
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        
        TODO: Add vertex to the adjacency list representation
        """
        # TODO: Implement this method
        pass
    
    def add_edge(self, vertex1, vertex2, directed=False):
        """
        Add an edge between two vertices.
        
        TODO: Implement edge addition
        - Add both vertices if they don't exist
        - Add edge from vertex1 to vertex2
        - If undirected, also add edge from vertex2 to vertex1
        """
        # TODO: Implement this method
        pass
    
    def get_vertices(self):
        """
        Get all vertices in the graph.
        
        TODO: Return a list of all vertices
        """
        # TODO: Implement this method
        pass
    
    def get_neighbors(self, vertex):
        """
        Get neighbors of a vertex.
        
        TODO: Return list of neighbors for the given vertex
        """
        # TODO: Implement this method
        pass
    
    def dfs(self, start):
        """
        Perform Depth-First Search starting from given vertex.
        
        TODO: Implement DFS traversal
        - Use recursion or stack
        - Keep track of visited vertices
        - Return list of vertices in DFS order
        """
        # TODO: Implement this method
        pass
    
    def bfs(self, start):
        """
        Perform Breadth-First Search starting from given vertex.
        
        TODO: Implement BFS traversal
        - Use queue for level-by-level traversal
        - Keep track of visited vertices
        - Return list of vertices in BFS order
        """
        # TODO: Implement this method
        pass
    
    def has_path(self, start, end):
        """
        Check if there's a path between start and end vertices.
        
        TODO: Implement path detection
        - Use DFS or BFS to check connectivity
        - Return True if path exists, False otherwise
        """
        # TODO: Implement this method
        pass

# Exercise 4: Tree Algorithms
def tree_height(root):
    """
    Calculate the height of a binary tree.
    
    TODO: Implement tree height calculation
    - Height is the longest path from root to any leaf
    - Empty tree has height -1 or 0 (choose one convention)
    - Single node has height 0 or 1 (choose one convention)
    """
    # TODO: Implement this function
    pass

def is_valid_bst(root):
    """
    Check if a binary tree is a valid Binary Search Tree.
    
    TODO: Implement BST validation
    - For each node, all left subtree values < node value
    - For each node, all right subtree values > node value
    - Consider using min/max bounds approach
    """
    # TODO: Implement this function
    pass

def lowest_common_ancestor(root, p, q):
    """
    Find the Lowest Common Ancestor of two nodes in a BST.
    
    TODO: Implement LCA finding
    - LCA is the deepest node that has both p and q as descendants
    - Use BST property to navigate efficiently
    """
    # TODO: Implement this function
    pass

# Exercise 5: Graph Algorithms
def detect_cycle(graph):
    """
    Detect if there's a cycle in an undirected graph.
    
    TODO: Implement cycle detection
    - Use DFS with parent tracking
    - If we visit a node that's already visited and it's not the parent, there's a cycle
    """
    # TODO: Implement this function
    pass

def shortest_path_unweighted(graph, start, end):
    """
    Find shortest path between two vertices in an unweighted graph.
    
    TODO: Implement shortest path finding
    - Use BFS to find shortest path
    - Return the path as a list of vertices
    - Return empty list if no path exists
    """
    # TODO: Implement this function
    pass

def connected_components(graph):
    """
    Find all connected components in an undirected graph.
    
    TODO: Implement connected components finding
    - Use DFS or BFS to explore each component
    - Return list of components, where each component is a list of vertices
    """
    # TODO: Implement this function
    pass

# Test functions
def test_binary_tree():
    """Test Binary Tree implementation"""
    print("Testing Binary Tree...")
    
    bt = BinaryTree()
    values = [1, 2, 3, 4, 5, 6, 7]
    
    for val in values:
        bt.insert_level_order(val)
    
    print("Level-order traversal:", bt.level_order_traversal())
    print("Inorder traversal:", bt.inorder_traversal())
    
    # Expected level-order: [1, 2, 3, 4, 5, 6, 7]
    # Expected inorder: [4, 2, 5, 1, 6, 3, 7]

def test_bst():
    """Test Binary Search Tree implementation"""
    print("\nTesting Binary Search Tree...")
    
    bst = BST()
    values = [5, 3, 7, 2, 4, 6, 8]
    
    for val in values:
        bst.insert(val)
    
    print("Search 4:", bst.search(4))  # Should be True
    print("Search 9:", bst.search(9))  # Should be False
    print("Min value:", bst.find_min())  # Should be 2
    print("Max value:", bst.find_max())  # Should be 8

def test_graph():
    """Test Graph implementation"""
    print("\nTesting Graph...")
    
    g = Graph()
    
    # Create a simple graph: A-B-C-D with A-C connection
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('C', 'D')
    g.add_edge('A', 'C')
    
    print("Vertices:", g.get_vertices())
    print("Neighbors of A:", g.get_neighbors('A'))
    print("DFS from A:", g.dfs('A'))
    print("BFS from A:", g.bfs('A'))
    print("Path A to D:", g.has_path('A', 'D'))  # Should be True
    print("Path A to E:", g.has_path('A', 'E'))  # Should be False

def test_tree_algorithms():
    """Test tree algorithms"""
    print("\nTesting Tree Algorithms...")
    
    # Create a simple BST: 5 -> 3,7 -> 2,4,6,8
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    
    print("Tree height:", tree_height(root))  # Should be 2
    print("Is valid BST:", is_valid_bst(root))  # Should be True
    print("LCA of 2 and 4:", lowest_common_ancestor(root, 2, 4))  # Should be 3

def test_graph_algorithms():
    """Test graph algorithms"""
    print("\nTesting Graph Algorithms...")
    
    # Create test graph
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('C', 'A')  # Creates a cycle
    g.add_edge('D', 'E')  # Separate component
    
    print("Has cycle:", detect_cycle(g))  # Should be True
    print("Shortest path A to C:", shortest_path_unweighted(g, 'A', 'C'))
    print("Connected components:", connected_components(g))

if __name__ == "__main__":
    print("Trees and Graphs Exercises")
    print("=" * 40)
    
    # Run tests (these will fail until you implement the functions)
    try:
        test_binary_tree()
    except Exception as e:
        print(f"Binary Tree test failed: {e}")
    
    try:
        test_bst()
    except Exception as e:
        print(f"BST test failed: {e}")
    
    try:
        test_graph()
    except Exception as e:
        print(f"Graph test failed: {e}")
    
    try:
        test_tree_algorithms()
    except Exception as e:
        print(f"Tree algorithms test failed: {e}")
    
    try:
        test_graph_algorithms()
    except Exception as e:
        print(f"Graph algorithms test failed: {e}")
    
    print("\nComplete the TODO sections to make all tests pass!")