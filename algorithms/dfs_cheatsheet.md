### How to Structure DFS

DFS typically involves three core components: a base case, a recursive step, and state management. Here’s how to build it:

1. Base Case
   The base case defines when to stop exploring. Common examples include:
   Trees: Reaching a null or leaf node (if node is None).

\***\*Graphs**: Encountering a visited node (if node in visited).

**Goal Reached**: Finding the target (e.g., destination in a maze).

**Invalid State**: Out-of-bounds in a grid or an invalid move.

2. Recursive Case
   This is the heart of DFS—calling the function on the next level or neighbor. For example:
   In a tree, recurse on left and right children.

In a graph, recurse on all unvisited neighbors.

In a grid, recurse on adjacent cells (up, down, left, right).

3. State Management
   Track the current state to avoid getting lost. This might include:
   Visited Set: For graphs, to prevent revisiting nodes (e.g., visited = set()).

**Path**: The sequence of nodes or moves so far.

**Position**: Current coordinates in a grid.

**Results**: Accumulating solutions (e.g., all valid permutations).

### Basic DFS Template (Tree)

Here’s a simple DFS for a binary tree (pre-order traversal):

```python

def dfs(node):
    if node is None: # Base case
        return

    print(node.value) # Process current node
    dfs(node.left) # Recurse left
    dfs(node.right) # Recurse right
```

### General DFS Template (Graph)

For graphs, add a visited set to handle cycles:

```python

def dfs(graph, node, visited):
    if node in visited:  # Base case
        return

    visited.add(node)
    print(node)  # Process current node
    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)  # Recurse on neighbors

```
