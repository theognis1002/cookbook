"""
    Depth-First Search (DFS) - Recursive Implementation
    Description:
    This is a recursive implementation of the Depth-First Search (DFS) algorithm for traversing or 
    searching tree or graph data structures. The algorithm starts at the root node (or an arbitrary node 
    in the case of a graph) and explores as far as possible along each branch before backtracking.

    Key Differences from Iterative (Stack-based) Implementation:
    - Uses system call stack instead of explicit stack data structure
    - More elegant and concise implementation
    - May hit recursion depth limit for very deep graphs
    - Generally uses more memory due to stack frames

    When/Why to Use Recursive DFS:
    - When code clarity is prioritized over memory efficiency
    - When working with trees or graphs that won't exceed recursion depth
    - When needing to maintain state during traversal
    - When implementing backtracking algorithms

    Adjacency list:
    graph = {
        0: [1, 2],
        1: [3, 4],
        2: [5],
        3: [],
        4: [6],
        5: [],
        6: []
    }

    Graphical representation:
         0
        / \
       1   2
      / \   \
     3   4   5
              \
               6
"""


def dfs_recursive(graph, node, visited=None):
    # Initialize visited set on first call
    if visited is None:
        visited = set()

    # Mark current node as visited and print it
    visited.add(node)
    print(node)

    # Recursively visit all unvisited neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


# Example usage
if __name__ == "__main__":
    # Example graph from the documentation
    graph = {0: [1, 2], 1: [3, 4], 2: [5], 3: [], 4: [6], 5: [], 6: []}

    dfs_recursive(graph, 0)
