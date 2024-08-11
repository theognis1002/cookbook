"""
Dijkstra's Algorithm Implementation

This module implements Dijkstra's algorithm to find the shortest path from a starting node to all other nodes in a weighted graph.

Dijkstra's Algorithm:
- Dijkstra's algorithm is used to find the shortest path between nodes in a graph. It works by iteratively selecting the node with the smallest known distance from the start node, updating the distances to its neighbors, and repeating this process until all nodes have been processed.

Steps to Implement Dijkstra's Algorithm:
1. Initialize distances from the start node to all other nodes as infinity, except the start node itself, which is set to 0.
2. Use a priority queue to keep track of nodes to be visited, prioritized by their current known distance.
3. Pop the node with the smallest distance from the priority queue and explore its neighbors.
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
    distances = find_shortest_path(graph, "A")
    print(distances)  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
"""

import heapq


def find_shortest_path(graph, start):
    """
    Find the shortest path from the start node to all other nodes in a graph using Dijkstra's algorithm.

    Parameters:
    graph (dict): A dictionary where keys are node names and values are dictionaries of neighboring nodes and their edge weights.
    start (str): The starting node for the algorithm.

    Returns:
    dict: A dictionary where keys are node names and values are the shortest distance from the start node.
    """
    # Initialize distances from start node to all nodes as infinity
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    # Priority queue to visit nodes based on the shortest known distance
    to_visit = []
    heapq.heappush(to_visit, (0, start))

    while to_visit:
        # Pop the node with the smallest distance from the priority queue
        current_cost, current_node = heapq.heappop(to_visit)

        # Skip processing if a shorter path to current_node is already known
        if distances[current_node] < current_cost:
            continue

        # Explore neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            new_cost = current_cost + weight

            # If a shorter path to neighbor is found, update the distance and push to the queue
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                heapq.heappush(to_visit, (new_cost, neighbor))

    return distances


if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {"A": {"B": 1, "C": 5}, "B": {"C": 2, "D": 3}, "C": {"D": 4}, "D": {"A": 6}}

    # Find the shortest path from node "A" to all other nodes
    distances = find_shortest_path(graph, "A")
    print(distances)
