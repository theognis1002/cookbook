"""
    Depth-First Search (DFS)
    Description:
    Depth-First Search (DFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the root node (or an arbitrary node in the case of a graph) and explores as far as possible along each branch before backtracking.

    When/Why to Use DFS:

    Path Finding: DFS is useful for finding a path between two nodes in a graph.
    Topological Sorting: DFS is used for topological sorting of a Directed Acyclic Graph (DAG).
    Detecting Cycles in Directed Graphs: DFS can detect cycles in directed graphs by tracking the recursion stack.
    Solving Puzzles and Games: DFS is often used in puzzles and games where all possible moves need to be explored, such as maze solving and Sudoku.
    Tree Traversal: DFS can be used for pre-order, in-order, and post-order tree traversals.

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


def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)

            for child_node in graph[node]:
                if child_node not in visited:
                    stack.append(child_node)
