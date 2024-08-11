import collections


def convert_file_into_matrix(file_path: str) -> list[list[int]]:
    """Read text file and convert to matrix (list of lists).

    Args:
        file_path (str): input text file

    Returns:
        list[list[int]]: matrix
    """
    matrix = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            matrix.append([int(char) for char in line.strip()])
    return matrix


def calculate_shapes(matrix: list[list[int]]) -> int:
    """Given an input matrix, perform Breadth-First-Search (BFS) and check adjacent positions
    to see if there is a new shape consisting of 1's.

    Args:
        matrix (list[list[str]]): input matrix

    Returns:
        int: # of shapes
    """
    num_shapes = 0
    visited = set()
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    def bfs(row, col):
        q = collections.deque([(row, col)])
        visited.add((row, col))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # right, left, up, down

        while q:
            row, col = q.popleft()
            for x_coord, y_coord in directions:
                adj_row = row + x_coord
                adj_col = col + y_coord
                if (
                    0 <= adj_row < num_rows
                    and 0 <= adj_col < num_cols
                    and matrix[adj_row][adj_col] == 1
                    and (adj_row, adj_col) not in visited
                ):
                    q.append((adj_row, adj_col))
                    visited.add((adj_row, adj_col))

    for row in range(num_rows):
        for col in range(num_cols):
            if matrix[row][col] == 1 and (row, col) not in visited:
                num_shapes += 1
                bfs(row, col)

    return num_shapes


if __name__ == "__main__":
    # matrix = [
    #     [0, 1, 1, 0],
    #     [0, 1, 0, 0],
    #     [0, 0, 1, 0],
    #     [0, 0, 1, 1],
    # ]

    file_path = "../data/data_small.txt"
    matrix = convert_file_into_matrix(file_path)
    res1 = calculate_shapes(matrix)
    print(res1)  # 13

    file_path = "../data/data_large.txt"
    matrix = convert_file_into_matrix(file_path)
    res2 = calculate_shapes(matrix)
    print(res2)  # 663
