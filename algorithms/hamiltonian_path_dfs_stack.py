from collections import defaultdict


def has_hamiltonian_path(edges: list[list[int]], source: int, destination: int) -> bool:
    if source == destination:
        return True

    graph = defaultdict(list)
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)

    seen = set([source])
    stack = [source]

    while stack:
        node = stack.pop()
        if node == destination:
            return True

        for child_node in graph[node]:
            if child_node not in seen:
                seen.add(child_node)
                stack.append(node)

    return False
