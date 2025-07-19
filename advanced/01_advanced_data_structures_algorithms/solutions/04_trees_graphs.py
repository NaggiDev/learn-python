"""
Trees and Graphs Solutions

This file contains complete solutions for the trees and graphs exercises.
"""

# Solution 1: Binary Tree Implementation
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert_level_order(self, val):
        """Insert a value into the binary tree using level-order insertion."""
        if not self.root:
            self.root = TreeNode(val)
            return
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            
            if not node.left:
                node.left = TreeNode(val)
                return
            elif not node.right:
                node.right = TreeNode(val)
                return
            else:
                queue.append(node.left)
                queue.append(node.right)
    
    def inorder_traversal(self):
        """Perform inorder traversal of the binary tree."""
        def inorder_helper(node):
            if not node:
                return []
            
            result = []
            result.extend(inorder_helper(node.left))
            result.append(node.val)
            result.extend(inorder_helper(node.right))
            return result
        
        return inorder_helper(self.root)
    
    def level_order_traversal(self):
        """Perform level-order traversal of the binary tree."""
        if not self.root:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result

# Solution 2: Binary Search Tree Implementation
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        """Insert a value into the BST maintaining BST property."""
        self.root = self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node, val):
        if not node:
            return TreeNode(val)
        
        if val < node.val:
            node.left = self._insert_recursive(node.left, val)
        elif val > node.val:
            node.right = self._insert_recursive(node.right, val)
        # Ignore duplicates
        
        return node
    
    def search(self, val):
        """Search for a value in the BST."""
        return self._search_recursive(self.root, val)
    
    def _search_recursive(self, node, val):
        if not node:
            return False
        
        if node.val == val:
            return True
        elif val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)
    
    def find_min(self):
        """Find the minimum value in the BST."""
        if not self.root:
            return None
        
        current = self.root
        while current.left:
            current = current.left
        return current.val
    
    def find_max(self):
        """Find the maximum value in the BST."""
        if not self.root:
            return None
        
        current = self.root
        while current.right:
            current = current.right
        return current.val

# Solution 3: Graph Implementation
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2, directed=False):
        """Add an edge between two vertices."""
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        
        self.graph[vertex1].append(vertex2)
        if not directed:
            self.graph[vertex2].append(vertex1)
    
    def get_vertices(self):
        """Get all vertices in the graph."""
        return list(self.graph.keys())
    
    def get_neighbors(self, vertex):
        """Get neighbors of a vertex."""
        return self.graph.get(vertex, [])
    
    def dfs(self, start):
        """Perform Depth-First Search starting from given vertex."""
        visited = set()
        result = []
        
        def dfs_helper(vertex):
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor in self.get_neighbors(vertex):
                if neighbor not in visited:
                    dfs_helper(neighbor)
        
        if start in self.graph:
            dfs_helper(start)
        
        return result
    
    def bfs(self, start):
        """Perform Breadth-First Search starting from given vertex."""
        if start not in self.graph:
            return []
        
        visited = set()
        queue = [start]
        result = []
        
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                
                for neighbor in self.get_neighbors(vertex):
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return result
    
    def has_path(self, start, end):
        """Check if there's a path between start and end vertices."""
        if start not in self.graph or end not in self.graph:
            return False
        
        if start == end:
            return True
        
        visited = set()
        queue = [start]
        
        while queue:
            vertex = queue.pop(0)
            if vertex == end:
                return True
            
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return False

# Solution 4: Tree Algorithms
def tree_height(root):
    """Calculate the height of a binary tree."""
    if not root:
        return -1  # Convention: empty tree has height -1
    
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    
    return 1 + max(left_height, right_height)

def is_valid_bst(root):
    """Check if a binary tree is a valid Binary Search Tree."""
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (validate(node.left, min_val, node.val) and 
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))

def lowest_common_ancestor(root, p, q):
    """Find the Lowest Common Ancestor of two nodes in a BST."""
    if not root:
        return None
    
    # If both p and q are smaller than root, LCA is in left subtree
    if p < root.val and q < root.val:
        return lowest_common_ancestor(root.left, p, q)
    
    # If both p and q are greater than root, LCA is in right subtree
    if p > root.val and q > root.val:
        return lowest_common_ancestor(root.right, p, q)
    
    # If p and q are on different sides of root, root is the LCA
    return root.val

# Solution 5: Graph Algorithms
def detect_cycle(graph):
    """Detect if there's a cycle in an undirected graph."""
    visited = set()
    
    def dfs_cycle_check(vertex, parent):
        visited.add(vertex)
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                if dfs_cycle_check(neighbor, vertex):
                    return True
            elif neighbor != parent:
                # Found a back edge (cycle)
                return True
        
        return False
    
    # Check all components
    for vertex in graph.get_vertices():
        if vertex not in visited:
            if dfs_cycle_check(vertex, None):
                return True
    
    return False

def shortest_path_unweighted(graph, start, end):
    """Find shortest path between two vertices in an unweighted graph."""
    if start not in graph.graph or end not in graph.graph:
        return []
    
    if start == end:
        return [start]
    
    visited = set()
    queue = [(start, [start])]  # (vertex, path)
    
    while queue:
        vertex, path = queue.pop(0)
        
        if vertex == end:
            return path
        
        if vertex not in visited:
            visited.add(vertex)
            
            for neighbor in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    
    return []  # No path found

def connected_components(graph):
    """Find all connected components in an undirected graph."""
    visited = set()
    components = []
    
    def dfs_component(vertex, component):
        visited.add(vertex)
        component.append(vertex)
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                dfs_component(neighbor, component)
    
    for vertex in graph.get_vertices():
        if vertex not in visited:
            component = []
            dfs_component(vertex, component)
            components.append(component)
    
    return components

# Test functions
def test_binary_tree():
    """Test Binary Tree implementation"""
    print("Testing Binary Tree...")
    
    bt = BinaryTree()
    values = [1, 2, 3, 4, 5, 6, 7]
    
    for val in values:
        bt.insert_level_order(val)
    
    level_order = bt.level_order_traversal()
    inorder = bt.inorder_traversal()
    
    print("Level-order traversal:", level_order)
    print("Inorder traversal:", inorder)
    
    assert level_order == [1, 2, 3, 4, 5, 6, 7], f"Expected [1, 2, 3, 4, 5, 6, 7], got {level_order}"
    assert inorder == [4, 2, 5, 1, 6, 3, 7], f"Expected [4, 2, 5, 1, 6, 3, 7], got {inorder}"
    print("✓ Binary Tree tests passed!")

def test_bst():
    """Test Binary Search Tree implementation"""
    print("\nTesting Binary Search Tree...")
    
    bst = BST()
    values = [5, 3, 7, 2, 4, 6, 8]
    
    for val in values:
        bst.insert(val)
    
    search_4 = bst.search(4)
    search_9 = bst.search(9)
    min_val = bst.find_min()
    max_val = bst.find_max()
    
    print("Search 4:", search_4)
    print("Search 9:", search_9)
    print("Min value:", min_val)
    print("Max value:", max_val)
    
    assert search_4 == True, f"Expected True, got {search_4}"
    assert search_9 == False, f"Expected False, got {search_9}"
    assert min_val == 2, f"Expected 2, got {min_val}"
    assert max_val == 8, f"Expected 8, got {max_val}"
    print("✓ BST tests passed!")

def test_graph():
    """Test Graph implementation"""
    print("\nTesting Graph...")
    
    g = Graph()
    
    # Create a simple graph: A-B-C-D with A-C connection
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('C', 'D')
    g.add_edge('A', 'C')
    
    vertices = sorted(g.get_vertices())
    neighbors_a = sorted(g.get_neighbors('A'))
    dfs_result = g.dfs('A')
    bfs_result = g.bfs('A')
    path_a_to_d = g.has_path('A', 'D')
    path_a_to_e = g.has_path('A', 'E')
    
    print("Vertices:", vertices)
    print("Neighbors of A:", neighbors_a)
    print("DFS from A:", dfs_result)
    print("BFS from A:", bfs_result)
    print("Path A to D:", path_a_to_d)
    print("Path A to E:", path_a_to_e)
    
    assert set(vertices) == {'A', 'B', 'C', 'D'}, f"Expected A,B,C,D, got {vertices}"
    assert set(neighbors_a) == {'B', 'C'}, f"Expected B,C, got {neighbors_a}"
    assert len(dfs_result) == 4 and 'A' in dfs_result, f"DFS should visit all 4 nodes starting with A"
    assert len(bfs_result) == 4 and 'A' in bfs_result, f"BFS should visit all 4 nodes starting with A"
    assert path_a_to_d == True, f"Expected True, got {path_a_to_d}"
    assert path_a_to_e == False, f"Expected False, got {path_a_to_e}"
    print("✓ Graph tests passed!")

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
    
    height = tree_height(root)
    is_bst = is_valid_bst(root)
    lca = lowest_common_ancestor(root, 2, 4)
    
    print("Tree height:", height)
    print("Is valid BST:", is_bst)
    print("LCA of 2 and 4:", lca)
    
    assert height == 2, f"Expected 2, got {height}"
    assert is_bst == True, f"Expected True, got {is_bst}"
    assert lca == 3, f"Expected 3, got {lca}"
    print("✓ Tree algorithm tests passed!")

def test_graph_algorithms():
    """Test graph algorithms"""
    print("\nTesting Graph Algorithms...")
    
    # Create test graph with cycle
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('C', 'A')  # Creates a cycle
    g.add_edge('D', 'E')  # Separate component
    
    has_cycle = detect_cycle(g)
    shortest_path = shortest_path_unweighted(g, 'A', 'C')
    components = connected_components(g)
    
    print("Has cycle:", has_cycle)
    print("Shortest path A to C:", shortest_path)
    print("Connected components:", components)
    
    assert has_cycle == True, f"Expected True, got {has_cycle}"
    assert len(shortest_path) >= 2 and shortest_path[0] == 'A' and shortest_path[-1] == 'C', f"Path should start with A and end with C"
    assert len(components) == 2, f"Expected 2 components, got {len(components)}"
    print("✓ Graph algorithm tests passed!")

if __name__ == "__main__":
    print("Trees and Graphs Solutions")
    print("=" * 40)
    
    test_binary_tree()
    test_bst()
    test_graph()
    test_tree_algorithms()
    test_graph_algorithms()
    
    print("\n🎉 All tests passed! Solutions are working correctly.")