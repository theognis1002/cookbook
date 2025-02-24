"""
1. Transpose a Matrix

Swaps rows with columns.
"""


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    m = len(matrix[0])
    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][i] = matrix[i][j]

    return result


"""
Before:

1  2  3
4  5  6
7  8  9

After (Transpose):

1  4  7
2  5  8
3  6  9
"""

"""
2. Rotate 90 Degrees Clockwise

Transpose first, then reverse each row.
"""


def rotate_90_clockwise(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    m = len(matrix[0])
    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n - 1 - i] = matrix[i][j]

    return result


"""
Before:

1  2  3
4  5  6
7  8  9

After (90° Clockwise):

7  4  1
8  5  2
9  6  3
"""

"""
3. Rotate 90 Degrees Counterclockwise

Transpose first, then reverse each column.
"""


def rotate_90_counterclockwise(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    m = len(matrix[0])
    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[m - 1 - j][i] = matrix[i][j]

    return result


"""
Before:

1  2  3
4  5  6
7  8  9

After (90° Counterclockwise):

3  6  9
2  5  8
1  4  7
"""

"""
4. Reflect Horizontally (Flip Upside Down)

Reverse row order.
"""


def reflect_horizontally(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    m = len(matrix[0])
    result = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            result[n - 1 - i][j] = matrix[i][j]

    return result


"""
Before:

1  2  3
4  5  6
7  8  9

After (Flipped Horizontally):

7  8  9
4  5  6
1  2  3
"""

"""
5. Reflect Vertically (Mirror Image)

Reverse column order.
"""


def reflect_vertically(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    m = len(matrix[0])
    result = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            result[i][m - 1 - j] = matrix[i][j]

    return result


"""
Before:

1  2  3
4  5  6
7  8  9

After (Flipped Vertically):

3  2  1
6  5  4
9  8  7
"""

"""
6. Rotate 180 Degrees

Reverse both rows and columns.
"""


def rotate_180(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    m = len(matrix[0])
    result = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            result[n - 1 - i][m - 1 - j] = matrix[i][j]

    return result


"""
Before:

1  2  3
4  5  6
7  8  9

After (180° Rotation):

9  8  7
6  5  4
3  2  1
"""
