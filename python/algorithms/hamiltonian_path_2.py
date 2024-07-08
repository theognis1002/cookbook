class Pathfinder:
    def __init__(self, graph):
        self.graph = graph
        self.paths = []

    @property
    def graph_size(self):
        return len(self.graph)

    def dfs(self, node, path):
        if len(path) == self.graph_size:
            self.paths.append(path[:])
            return

        for neighbor in self.graph[node]:
            if neighbor not in path:
                path.append(neighbor)
                self.dfs(neighbor, path)
                path.pop()

    def find_hamiltonian_paths(self):
        for start in range(self.graph_size):
            self.dfs(start, [start])

        return self.paths


if __name__ == "__main__":
    graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    path_finder = Pathfinder(graph)
    paths = path_finder.find_hamiltonian_paths()
    print(paths)
