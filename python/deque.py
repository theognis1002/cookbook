"""
Python’s deque is a low-level and highly optimized double-ended queue that’s useful for implementing elegant, efficient, and Pythonic queues and stacks, which are the most common list-like data types in computing.

See ring buffer (circular buffers) in low-level programming languages like C++, Java.
https://en.wikipedia.org/wiki/Circular_buffer
"""
from collections import deque

numbers = deque([1, 2, 3, 4])
numbers.popleft()
# 1
numbers.popleft()
# 2
numbers
# deque([3, 4])

numbers.appendleft(2)
numbers.appendleft(1)
numbers
# deque([1, 2, 3, 4])
