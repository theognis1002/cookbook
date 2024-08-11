"""
A* Algorithm Implementation

This module implements the A* algorithm to find the shortest path from a starting node to all other nodes in a weighted graph.

A* Algorithm:
- A* algorithm is used to find the shortest path between nodes in a graph. It combines Dijkstra's algorithm with heuristics to prioritize which nodes to explore.

Steps to Implement A* Algorithm:
1. Initialize distances from the start node to all other nodes as infinity, except the start node itself, which is set to 0.
2. Use a priority queue to keep track of nodes to be visited, prioritized by the sum of the current known distance and the heuristic estimate.
3. Pop the node with the smallest priority from the priority queue and explore its neighbors.
4. For each neighbor, calculate the tentative distance through the current node.
5. If the tentative distance is smaller than the known distance, update the distance and add the neighbor to the priority queue.
6. Repeat steps 3-5 until the priority queue is empty.
7. Return the distances from the start node to all other nodes.

Example Usage:
    graph = {
        "A": {"B": 1, "C": 5},
        "B": {"C": 2, "D": 3},
        "C": {"D": 4},
        "D": {"A": 6}
    }
    heuristic = {
        "A": 7,
        "B": 6,
        "C": 2,
        "D": 1
    }
    distances = find_shortest_path(graph, heuristic, "A", "D")
    print(distances)  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
"""

import heapq


def find_shortest_path(graph, heuristic, start, goal):
    """
    Find the shortest path from the start node to all other nodes in a graph using the A* algorithm.

    Parameters:
    graph (dict): A dictionary where keys are node names and values are dictionaries of neighboring nodes and their edge weights.
    heuristic (dict): A dictionary where keys are node names and values are the heuristic estimate to the goal node.
    start (str): The starting node for the algorithm.
    goal (str): The goal node for the algorithm.

    Returns:
    dict: A dictionary where keys are node names and values are the shortest distance from the start node.
    """
    # Initialize distances from start node to all nodes as infinity
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    # Priority queue to visit nodes based on the shortest known distance plus heuristic
    to_visit = []
    heapq.heappush(to_visit, (0 + heuristic[start], start))

    while to_visit:
        # Pop the node with the smallest priority from the priority queue
        current_priority, current_node = heapq.heappop(to_visit)

        # If we reached the goal node, return the distances
        if current_node == goal:
            return distances

        # Explore neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            new_cost = distances[current_node] + weight

            # If a shorter path to neighbor is found, update the distance and push to the queue
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(to_visit, (priority, neighbor))

    return distances


if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {"A": {"B": 1, "C": 5}, "B": {"C": 2, "D": 3}, "C": {"D": 4}, "D": {"A": 6}}

    # Example heuristic for each node
    heuristic = {"A": 7, "B": 6, "C": 2, "D": 1}

    # Find the shortest path from node "A" to node "D"
    distances = find_shortest_path(graph, heuristic, "A", "D")
    print(distances)
