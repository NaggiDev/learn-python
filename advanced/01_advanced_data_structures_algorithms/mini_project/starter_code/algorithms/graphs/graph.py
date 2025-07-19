"""
Graph Data Structure Implementation

This module implements graph data structure with both adjacency list and
adjacency matrix representations, supporting both directed and undirected graphs.
"""

from typing import Dict, List, Set, Optional, Tuple
import numpy as np


class Graph:
    """
    Graph implementation supporting both adjacency list and matrix representations.
    
    Supports both directed and undirected graphs with weighted edges.
    """
    
    def __init__(self, directed: bool = False, weighted: bool = False):
        """
        Initialize a graph.
        
        Args:
            directed: Whether the graph is directed
            weighted: Whether the graph has weighted edges
        """
        self.directed = directed
        self.weighted = weighted
        self.adjacency_list: Dict[str, List[Tuple[str, float]]] = {}
        self.vertices: Set[str] = set()
        self._adjacency_matrix: Optional[np.ndarray] = None
        self._vertex_to_index: Dict[str, int] = {}
        self._index_to_vertex: Dict[int, str] = {}
    
    def add_vertex(self, vertex: str) -> None:
        """
        Add a vertex to the graph.
        
        Args:
            vertex: Vertex identifier
            
        Time Complexity: O(1)
        """
        # TODO: Add vertex to the graph
        # Update adjacency list and vertex set
        # Invalidate adjacency matrix if it exists
        pass
    
    def add_edge(self, from_vertex: str, to_vertex: str, weight: float = 1.0) -> None:
        """
        Add an edge to the graph.
        
        Args:
            from_vertex: Source vertex
            to_vertex: Destination vertex
            weight: Edge weight (default 1.0)
            
        Time Complexity: O(1)
        """
        # TODO: Add edge to the graph
        # Add vertices if they don't exist
        # Add edge to adjacency list
        # For undirected graphs, add edge in both directions
        # Invalidate adjacency matrix
        pass
    
    def remove_vertex(self, vertex: str) -> bool:
        """
        Remove a vertex and all its edges from the graph.
        
        Args:
            vertex: Vertex to remove
            
        Returns:
            True if vertex was removed, False if not found
            
        Time Complexity: O(V + E) where V is vertices, E is edges
        """
        # TODO: Remove vertex and all associated edges
        pass
    
    def remove_edge(self, from_vertex: str, to_vertex: str) -> bool:
        """
        Remove an edge from the graph.
        
        Args:
            from_vertex: Source vertex
            to_vertex: Destination vertex
            
        Returns:
            True if edge was removed, False if not found
            
        Time Complexity: O(degree of from_vertex)
        """
        # TODO: Remove edge from adjacency list
        # For undirected graphs, remove from both directions
        pass
    
    def has_vertex(self, vertex: str) -> bool:
        """
        Check if vertex exists in the graph.
        
        Args:
            vertex: Vertex to check
            
        Returns:
            True if vertex exists
            
        Time Complexity: O(1)
        """
        # TODO: Check if vertex exists
        pass
    
    def has_edge(self, from_vertex: str, to_vertex: str) -> bool:
        """
        Check if edge exists in the graph.
        
        Args:
            from_vertex: Source vertex
            to_vertex: Destination vertex
            
        Returns:
            True if edge exists
            
        Time Complexity: O(degree of from_vertex)
        """
        # TODO: Check if edge exists in adjacency list
        pass
    
    def get_neighbors(self, vertex: str) -> List[Tuple[str, float]]:
        """
        Get all neighbors of a vertex with edge weights.
        
        Args:
            vertex: Vertex to get neighbors for
            
        Returns:
            List of (neighbor, weight) tuples
            
        Time Complexity: O(1)
        """
        # TODO: Return neighbors from adjacency list
        pass
    
    def get_edge_weight(self, from_vertex: str, to_vertex: str) -> Optional[float]:
        """
        Get the weight of an edge.
        
        Args:
            from_vertex: Source vertex
            to_vertex: Destination vertex
            
        Returns:
            Edge weight if edge exists, None otherwise
            
        Time Complexity: O(degree of from_vertex)
        """
        # TODO: Find and return edge weight
        pass
    
    def get_adjacency_matrix(self) -> np.ndarray:
        """
        Get the adjacency matrix representation of the graph.
        
        Returns:
            Adjacency matrix as numpy array
            
        Time Complexity: O(V²) to build, O(1) if cached
        """
        # TODO: Build and cache adjacency matrix
        # Use infinity for non-existent edges in weighted graphs
        # Use 0/1 for unweighted graphs
        pass
    
    def _build_adjacency_matrix(self) -> None:
        """Build the adjacency matrix from adjacency list."""
        # TODO: Convert adjacency list to matrix representation
        pass
    
    def get_vertices(self) -> List[str]:
        """
        Get all vertices in the graph.
        
        Returns:
            List of all vertices
            
        Time Complexity: O(V)
        """
        # TODO: Return list of all vertices
        pass
    
    def get_edges(self) -> List[Tuple[str, str, float]]:
        """
        Get all edges in the graph.
        
        Returns:
            List of (from_vertex, to_vertex, weight) tuples
            
        Time Complexity: O(E)
        """
        # TODO: Return list of all edges
        # For undirected graphs, include each edge only once
        pass
    
    def vertex_count(self) -> int:
        """
        Get the number of vertices in the graph.
        
        Returns:
            Number of vertices
            
        Time Complexity: O(1)
        """
        return len(self.vertices)
    
    def edge_count(self) -> int:
        """
        Get the number of edges in the graph.
        
        Returns:
            Number of edges
            
        Time Complexity: O(V)
        """
        # TODO: Count total number of edges
        # For undirected graphs, each edge is stored twice in adjacency list
        pass
    
    def is_connected(self) -> bool:
        """
        Check if the graph is connected (for undirected graphs).
        
        Returns:
            True if graph is connected
            
        Time Complexity: O(V + E)
        """
        # TODO: Use DFS/BFS to check connectivity
        # For directed graphs, check weak connectivity
        pass
    
    def __str__(self) -> str:
        """Return string representation of the graph."""
        graph_type = "Directed" if self.directed else "Undirected"
        weight_type = "Weighted" if self.weighted else "Unweighted"
        return f"{graph_type} {weight_type} Graph: {self.vertex_count()} vertices, {self.edge_count()} edges"
    
    def __repr__(self) -> str:
        """Return detailed representation of the graph."""
        return f"Graph(directed={self.directed}, weighted={self.weighted}, vertices={list(self.vertices)})"