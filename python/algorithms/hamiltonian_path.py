"""
A Hamiltonian path in a graph is a path that visits each vertex exactly once. Here’s an example problem statement similar to what you might find on LeetCode, along with a Python solution:

### Problem Statement:
Given an undirected graph represented as an adjacency list, determine if there exists a Hamiltonian path in the graph.

### Example:
```
Input: graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
Output: True
```

### Solution:
Here is a Python solution using a depth-first search (DFS) approach to find a Hamiltonian path:

"""


def has_hamiltonian_path(graph):
    n = len(graph)

    def dfs(node, visited):
        if len(visited) == n:
            return True

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                if dfs(neighbor, visited):
                    return True
                visited.remove(neighbor)

        return False

    for start in range(n):
        if dfs(start, {start}):
            return True

    return False


if __name__ == "__main__":
    # Example usage
    graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    print(has_hamiltonian_path(graph))  # Output: True
    breakpoint()

"""
### Explanation:
1. **Graph Representation:** The input graph is represented as an adjacency list. Each index represents a node, and the list at each index contains the neighbors of that node.
2. **DFS Function:** The `dfs` function performs a depth-first search to try to find a Hamiltonian path starting from the given node. It takes the current node and a set of visited nodes as arguments.
3. **Check All Nodes:** The outer loop attempts to start a DFS from each node in the graph to ensure all possible paths are considered.
4. **Base Case:** If the length of the visited set equals the number of nodes in the graph, a Hamiltonian path has been found.
5. **Recursive Case:** For each neighbor of the current node, if the neighbor has not been visited, it is added to the visited set, and the DFS continues from that neighbor. If a Hamiltonian path is found, `True` is returned. Otherwise, the neighbor is removed from the visited set, and the search continues.
6. **Result:** If a Hamiltonian path is found starting from any node, the function returns `True`. If no such path is found, it returns `False`.

This code efficiently searches for a Hamiltonian path using DFS and backtracking, ensuring that all possible paths are considered.
"""
