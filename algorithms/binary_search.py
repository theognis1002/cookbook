def binary_search(array: list[int], target: int) -> int:
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (right + left) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 50, 100], 99))  # Output: -1
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 50, 100], 100))  # Output: 11
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 50, 100], 2))  # Output: 1
