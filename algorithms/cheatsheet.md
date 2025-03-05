## Technical Interview Algorithms Cheat Sheet (with Use Cases)

### Two Pointers

**Use Cases:**

- ✅ Sorting-related problems
- ✅ Finding pairs (sum, difference, etc.)
- ✅ Removing duplicates
- ✅ Palindromes

**Example Problems:**

- Leetcode 167 - Two Sum II
- Leetcode 125 - Valid Palindrome
- Leetcode 26 - Remove Duplicates from Sorted Array

**Example: Finding Pair Sum in Sorted Array**

```python
def two_sum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]  # 1-based index
        elif s < target:
            left += 1
        else:
            right -= 1
    return []
```

### Sliding Window

**Use Cases:**

- ✅ Finding subarrays with max/min sum
- ✅ Longest substring with constraints
- ✅ String/Array problems involving a “window”

**Example Problems:**

- Leetcode 3 - Longest Substring Without Repeating Characters
- Leetcode 209 - Minimum Size Subarray Sum
- Leetcode 76 - Minimum Window Substring

**Example: Longest Substring Without Repeating Characters**

```python
def length_of_longest_substring(s):
    char_set = set()
    left = max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
```

### Binary Search

**Use Cases:**

- ✅ Searching in sorted arrays
- ✅ Finding an element with constraints
- ✅ Optimization problems

**Example Problems:**

- Leetcode 704 - Binary Search
- Leetcode 35 - Search Insert Position
- Leetcode 33 - Search in Rotated Sorted Array

**Example: Basic Binary Search**

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### Depth-First Search (DFS)

**Use Cases:**

- ✅ Graph traversal
- ✅ Backtracking (combinations, permutations)
- ✅ Tree traversal

**Example Problems:**

- Leetcode 200 - Number of Islands
- Leetcode 39 - Combination Sum
- Leetcode 104 - Maximum Depth of Binary Tree

**Example: DFS for Number of Islands**

```python
def num_islands(grid):
    if not grid:
    return 0
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
            return
        grid[r][c] = "0"
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                dfs(r, c)
                count += 1
    return count
```

### Breadth-First Search (BFS)

**Use Cases:**

- ✅ Shortest path in graphs
- ✅ Finding the minimum number of steps
- ✅ Level-order traversal in trees

**Example Problems:**

- Leetcode 102 - Binary Tree Level Order Traversal
- Leetcode 542 - 01 Matrix
- Leetcode 127 - Word Ladder

Example: BFS for Shortest Path

```python
from collections import deque

def shortest_path(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(0, 0, 0)]) # (row, col, steps)
    visited = set()

    while queue:
        r, c, steps = queue.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))

        if r == rows - 1 and c == cols - 1:
            return steps

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                queue.append((nr, nc, steps + 1))

    return -1
```

### Dynamic Programming (DP)

**Use Cases:**

- ✅ Fibonacci-style problems
- ✅ Subset sums / Partitioning
- ✅ Counting unique paths

**Example Problems:**

- Leetcode 70 - Climbing Stairs
- Leetcode 322 - Coin Change
- Leetcode 416 - Partition Equal Subset Sum

**Example: DP for Climbing Stairs**

```
def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0] \* (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

### Greedy Algorithm

**Use Cases:**

- ✅ Scheduling problems
- ✅ Interval merging
- ✅ Finding optimal solutions quickly

**Example Problems:**

- Leetcode 455 - Assign Cookies
- Leetcode 435 - Non-overlapping Intervals
- Leetcode 763 - Partition Labels

**Example: Greedy Interval Scheduling**

```python
def erase_overlap_intervals(intervals):
    intervals.sort(key=lambda x: x[1])
    count, last_end = 0, float('-inf')
    for start, end in intervals:
        if start >= last_end:
            last_end = end
        else:
            count += 1
    return count
```

### Final Takeaways

- Two Pointers → Array-based optimizations (sorting, searching)
- Sliding Window → Subarrays, substrings, max/min problems
- Binary Search → Sorted arrays, search problems
- DFS/BFS → Graphs, trees, grid traversal, and combinatorial/permutations
- Dynamic Programming → Overlapping subproblems, counting solutions
- Greedy → Local optimal choices for global optimization
