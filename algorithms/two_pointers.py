"""
Two Pointers Technique

Description:
The two pointers technique is an algorithmic pattern that uses two pointers to traverse an array
or sequence, typically moving towards each other or in the same direction based on certain conditions.

Common Applications:
1. Finding pairs in a sorted array
2. Reversing arrays
3. Detecting cycles in linked lists
4. Removing duplicates
5. Finding triplets that sum to a target

Example Problem:
Given a sorted array of integers, find two numbers that add up to a specific target.
Return their indices if found, otherwise return None.

Time Complexity: O(n)
Space Complexity: O(1)
"""


def find_pair_sum(arr, target):
    """
    Find a pair of numbers in a sorted array that sum to target.

    Args:
        arr (List[int]): Sorted array of integers
        target (int): Target sum to find

    Returns:
        tuple: Indices of the two numbers that sum to target, or None if not found
    """
    left = 0  # pointer starting from the beginning
    right = len(arr) - 1  # pointer starting from the end

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            # If sum is too small, move left pointer to increase sum
            left += 1
        else:
            # If sum is too large, move right pointer to decrease sum
            right -= 1

    return None


if __name__ == "__main__":
    # Example usage
    sorted_array = [1, 2, 3, 4, 6, 8, 9, 10]
    target_sum = 14

    result = find_pair_sum(sorted_array, target_sum)

    if result:
        left_idx, right_idx = result
        print(
            f"Found pair: {sorted_array[left_idx]} + {sorted_array[right_idx]} = {target_sum}"
        )
        print(f"At indices: {left_idx}, {right_idx}")
    else:
        print(f"No pair found that sums to {target_sum}")

    # Additional test cases
    print("\nMore examples:")
    test_cases = [
        ([1, 2, 3, 4, 5], 7),  # Should find 2 + 5
        ([1, 2, 3, 4, 5], 10),  # Should not find any pair
        ([1, 1, 2, 3, 4], 5),  # Should find 1 + 4
    ]

    for arr, target in test_cases:
        result = find_pair_sum(arr, target)
        if result:
            left_idx, right_idx = result
            print(f"Array: {arr}, Target: {target}")
            print(f"Found: {arr[left_idx]} + {arr[right_idx]} = {target}")
        else:
            print(f"Array: {arr}, Target: {target}")
            print("No pair found")
        print()
