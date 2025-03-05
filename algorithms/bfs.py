from collections import deque

"""
    Breadth-First Search (BFS)
    Description:
    Breadth-First Search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the root node (or an arbitrary node in the case of a graph) and explores all its neighboring nodes at the present depth before moving on to nodes at the next depth level.

    When/Why to Use BFS:

    Shortest Path in Unweighted Graphs: BFS is ideal for finding the shortest path in unweighted graphs because it explores all nodes at the present depth level before moving to the next depth level, ensuring the shortest path is found first.
    Level-Order Traversal in Trees: BFS is commonly used for level-order traversal of trees, which involves visiting nodes level by level from the root.
    Connected Components: BFS can be used to find all connected components in a graph.
    Cycle Detection in Undirected Graphs: BFS can detect cycles in undirected graphs by keeping track of visited nodes.

    Adjacency list:
    graph = {
        0: [1, 2],
        1: [3, 4],
        2: [5],
        3: [],
        4: [5],
        5: []
    }

    Graphical representation:
         0
        / \
       1   2
      / \   \
     3   4   5
              \
               5

"""


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node)

            # Add all the children of the current node to the queue
            for child_node in graph[node]:
                if child_node not in visited:
                    queue.append(child_node)


if __name__ == "__main__":
    graph = {0: [1, 2], 1: [3, 4], 2: [5], 3: [], 4: [5], 5: []}

    bfs(graph, 0)
