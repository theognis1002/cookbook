# Here are some common examples and use cases for **min-heaps** and **max-heaps** in Python using the `heapq` module:

### 1. **Min-Heap Example**:
# By default, `heapq` creates a min-heap. The smallest element is always at the root.

#### Use Case: Finding the k smallest elements in a list.

import heapq

nums = [5, 7, 9, 1, 3]

# Create a min-heap
heapq.heapify(nums)

# Get the smallest element (min-heap root)
smallest = heapq.heappop(nums)
print(smallest)  # Output: 1 (smallest element)

# Get the next smallest element
second_smallest = heapq.heappop(nums)
print(second_smallest)  # Output: 3

# To get the k smallest elements
nums = [5, 7, 9, 1, 3]
k_smallest = heapq.nsmallest(2, nums)
print(k_smallest)  # Output: [1, 3]

### 2. **Max-Heap Example**:
# Python's `heapq` only supports min-heaps natively. To create a **max-heap**, you can insert the negative of the values, which allows you to pop the largest values.

#### Use Case: Finding the k largest elements in a list.

nums = [5, 7, 9, 1, 3]

# Simulate a max-heap by pushing negative values
max_heap = [-n for n in nums]
heapq.heapify(max_heap)

# Get the largest element
largest = -heapq.heappop(max_heap)
print(largest)  # Output: 9 (largest element)

# Get the k largest elements using nlargest()
nums = [5, 7, 9, 1, 3]
k_largest = heapq.nlargest(2, nums)
print(k_largest)  # Output: [9, 7]

### 3. **Use Case: Merging Sorted Lists**:
# If you have multiple sorted lists, a min-heap can be used to merge them efficiently into one sorted list.

sorted_lists = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Merge sorted lists using heapq.merge()
merged = list(heapq.merge(*sorted_lists))
print(merged)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

### 4. **Use Case: Priority Queue**:
# You can use a heap to implement a priority queue where elements are processed based on their priority.

# Priority queue with tuples (priority, task)
tasks = [(3, "clean"), (1, "write code"), (2, "read")]

heapq.heapify(tasks)

# Process tasks by priority
while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"Priority {priority}: {task}")

# Output:
# Priority 1: write code
# Priority 2: read
# Priority 3: clean

### Summary:
# - **Min-heap**: By default, `heapq` creates a min-heap where the smallest element can be accessed or popped efficiently.
# - **Max-heap**: Simulated by pushing the negative of the values and popping the smallest (negative) to get the largest value.
# - Common use cases include finding the smallest/largest k elements, merging sorted lists, and building priority queues.
