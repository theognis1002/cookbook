"""
Problem: Maximum Sum of Subarray of Length k
- Given an array of integers and a number k, find the maximum sum of any contiguous subarray of length k.

Sliding Window Approach
1. Start by summing the first k elements to initialize the window.
2. Slide the window from the start to the end of the array by adding the next element to the window sum and subtracting the element that is left out of the window.

"""


def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return "Invalid input: k is larger than the length of the array"

    # Compute the sum of the first window of size k
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window from the start of the array to the end
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum


if __name__ == "__main__":
    # Example usage
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    print("Maximum sum of subarray of length", k, "is", max_sum_subarray(arr, k))
