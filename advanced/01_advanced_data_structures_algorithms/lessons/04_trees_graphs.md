# Trees and Graphs

## Learning Objectives

By the end of this lesson, you will be able to:
- Understand the fundamental concepts of tree and graph data structures
- Implement basic tree operations (insertion, traversal, search)
- Implement basic graph operations (traversal, pathfinding)
- Choose appropriate data structures for different problem scenarios
- Analyze the time and space complexity of tree and graph algorithms

## Introduction

Trees and graphs are fundamental non-linear data structures that model hierarchical and networked relationships respectively. They are essential for solving many real-world problems in computer science, from organizing file systems to social networks and routing algorithms.

## Trees

### What is a Tree?

A tree is a hierarchical data structure consisting of nodes connected by edges. It has the following properties:
- One node is designated as the root
- Every node (except the root) has exactly one parent
- Nodes can have zero or more children
- There are no cycles (no path from a node back to itself)

### Tree Terminology

- **Root**: The topmost node in the tree
- **Parent**: A node that has children
- **Child**: A node that has a parent
- **Leaf**: A node with no children
- **Subtree**: A tree formed by a node and all its descendants
- **Height**: The longest path from root to any leaf
- **Depth**: The distance from root to a specific node
- **Level**: All nodes at the same depth

### Binary Trees

A binary tree is a tree where each node has at most two children, typically called left and right children.

#### Binary Tree Implementation

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        """Insert a value into the binary tree (level-order insertion)"""
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
```

### Tree Traversals

Tree traversal is the process of visiting each node in the tree exactly once. There are several ways to traverse a tree:

#### Depth-First Traversals

1. **Inorder Traversal** (Left, Root, Right)
2. **Preorder Traversal** (Root, Left, Right)
3. **Postorder Traversal** (Left, Right, Root)

```python
def inorder_traversal(root):
    """Inorder traversal: Left -> Root -> Right"""
    result = []
    if root:
        result.extend(inorder_traversal(root.left))
        result.append(root.val)
        result.extend(inorder_traversal(root.right))
    return result

def preorder_traversal(root):
    """Preorder traversal: Root -> Left -> Right"""
    result = []
    if root:
        result.append(root.val)
        result.extend(preorder_traversal(root.left))
        result.extend(preorder_traversal(root.right))
    return result

def postorder_traversal(root):
    """Postorder traversal: Left -> Right -> Root"""
    result = []
    if root:
        result.extend(postorder_traversal(root.left))
        result.extend(postorder_traversal(root.right))
        result.append(root.val)
    return result
```

#### Breadth-First Traversal (Level Order)

```python
def level_order_traversal(root):
    """Level order traversal using queue"""
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result
```

### Binary Search Trees (BST)

A Binary Search Tree is a binary tree with the property that for each node:
- All values in the left subtree are less than the node's value
- All values in the right subtree are greater than the node's value

```python
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        """Insert a value into the BST"""
        self.root = self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node, val):
        if not node:
            return TreeNode(val)
        
        if val < node.val:
            node.left = self._insert_recursive(node.left, val)
        elif val > node.val:
            node.right = self._insert_recursive(node.right, val)
        
        return node
    
    def search(self, val):
        """Search for a value in the BST"""
        return self._search_recursive(self.root, val)
    
    def _search_recursive(self, node, val):
        if not node or node.val == val:
            return node
        
        if val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)
```

## Graphs

### What is a Graph?

A graph is a collection of vertices (nodes) connected by edges. Unlike trees, graphs can have cycles and multiple paths between nodes.

### Graph Terminology

- **Vertex/Node**: A point in the graph
- **Edge**: A connection between two vertices
- **Adjacent**: Two vertices connected by an edge
- **Degree**: Number of edges connected to a vertex
- **Path**: A sequence of vertices connected by edges
- **Cycle**: A path that starts and ends at the same vertex
- **Connected Graph**: Every vertex is reachable from every other vertex

### Types of Graphs

1. **Directed vs Undirected**: Edges have direction or not
2. **Weighted vs Unweighted**: Edges have weights/costs or not
3. **Connected vs Disconnected**: All vertices reachable or not

### Graph Representations

#### Adjacency List

```python
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph"""
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2, directed=False):
        """Add an edge between two vertices"""
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        
        self.graph[vertex1].append(vertex2)
        if not directed:
            self.graph[vertex2].append(vertex1)
    
    def get_vertices(self):
        """Get all vertices in the graph"""
        return list(self.graph.keys())
    
    def get_neighbors(self, vertex):
        """Get neighbors of a vertex"""
        return self.graph.get(vertex, [])
```

#### Adjacency Matrix

```python
class GraphMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]
    
    def add_edge(self, vertex1, vertex2, weight=1, directed=False):
        """Add an edge between two vertices"""
        self.matrix[vertex1][vertex2] = weight
        if not directed:
            self.matrix[vertex2][vertex1] = weight
    
    def has_edge(self, vertex1, vertex2):
        """Check if there's an edge between two vertices"""
        return self.matrix[vertex1][vertex2] != 0
```

### Graph Traversals

#### Depth-First Search (DFS)

```python
def dfs(graph, start, visited=None):
    """Depth-First Search traversal"""
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph.get_neighbors(start):
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    
    return result

def dfs_iterative(graph, start):
    """Iterative DFS using stack"""
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            # Add neighbors to stack (reverse order for consistent traversal)
            for neighbor in reversed(graph.get_neighbors(vertex)):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result
```

#### Breadth-First Search (BFS)

```python
def bfs(graph, start):
    """Breadth-First Search traversal"""
    visited = set()
    queue = [start]
    result = []
    
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return result
```

### Shortest Path Algorithms

#### Dijkstra's Algorithm (for weighted graphs)

```python
import heapq

def dijkstra(graph, start):
    """Find shortest paths from start vertex to all other vertices"""
    distances = {vertex: float('infinity') for vertex in graph.get_vertices()}
    distances[start] = 0
    
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        for neighbor, weight in graph.get_weighted_neighbors(current_vertex):
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances
```

## Common Applications

### Trees
- File systems (directory structure)
- Expression parsing
- Database indexing
- Decision trees in machine learning
- Huffman coding for compression

### Graphs
- Social networks
- Transportation networks
- Web page linking
- Dependency resolution
- Network routing protocols

## Time Complexity Analysis

### Tree Operations
- **Search in BST**: O(log n) average, O(n) worst case
- **Insert in BST**: O(log n) average, O(n) worst case
- **Tree Traversal**: O(n) for all traversal methods

### Graph Operations
- **DFS/BFS**: O(V + E) where V is vertices and E is edges
- **Dijkstra's Algorithm**: O((V + E) log V) with priority queue

## Best Practices

1. **Choose the right representation**: Adjacency list for sparse graphs, adjacency matrix for dense graphs
2. **Consider balance**: Use self-balancing trees (AVL, Red-Black) for guaranteed performance
3. **Handle edge cases**: Empty trees/graphs, single nodes, disconnected components
4. **Memory efficiency**: Be mindful of space complexity, especially with large graphs
5. **Cycle detection**: Important for many graph algorithms to avoid infinite loops

## Summary

Trees and graphs are powerful data structures that model hierarchical and networked relationships. Understanding their properties, implementations, and algorithms is crucial for solving complex computational problems. Practice implementing these structures and their associated algorithms to build intuition for when and how to use them effectively.