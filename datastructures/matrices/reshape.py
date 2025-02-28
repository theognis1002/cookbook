def matrix_reshape(
    matrix: list[list[int]], new_rows: int, new_cols: int
) -> list[list[int]]:
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    if num_rows * num_cols != new_rows * new_cols:
        return matrix

    flattened_matrix = []
    for i in range(num_rows):
        for j in range(num_cols):
            flattened_matrix.append(matrix[i][j])

    reshaped_matrix = []
    k = 0
    for i in range(new_rows):
        row = []
        for j in range(new_cols):
            row.append(flattened_matrix[k])
            k += 1
        reshaped_matrix.append(row)

    return reshaped_matrix


if __name__ == "__main__":
    matrix = [[1, 2], [3, 4]]
    new_rows = 1
    new_cols = 4
    print(matrix_reshape(matrix, new_rows, new_cols))
    # [[1, 2, 3, 4]]
