# Python Asyncio Guide

## 1. Async Basics & Event Loop

### Q1: Explain how Python's asyncio event loop works.

**Answer:**

- The event loop is the core of async Python, managing asynchronous tasks and I/O operations.
- It runs a single thread and schedules coroutines using cooperative multitasking.
- Instead of blocking on I/O, the loop suspends a coroutine and resumes it once the awaited task completes.

**Follow-up:** What happens if you block the event loop with a synchronous operation?

**Answer:**

- If you block the event loop with a long-running synchronous operation (e.g., `time.sleep(5)`), the event loop pauses all tasks until the blocking function finishes.
- Instead, use `await asyncio.sleep(5)` to prevent blocking.

## 2. Async vs. Threading vs. Multiprocessing

### Q2: How does async Python compare to threading and multiprocessing?

**Answer:**

| Feature     | Async (asyncio)        | Threading (threading)     | Multiprocessing (multiprocessing) |
| ----------- | ---------------------- | ------------------------- | --------------------------------- |
| Concurrency | Yes (non-blocking I/O) | Yes (context switching)   | No (separate processes)           |
| Parallelism | No (single thread)     | No (GIL limits execution) | Yes (bypasses GIL)                |
| Best For    | I/O-bound tasks        | Mixed workloads           | CPU-bound tasks                   |

- Async Python is best for I/O-bound tasks like HTTP requests or DB queries.
- Threading is useful when dealing with I/O but has overhead due to context switching.
- Multiprocessing is better for CPU-bound tasks because it bypasses Python's GIL.

**Follow-up:** When would you choose async over threads or processes?

**Answer:**

- Use async when dealing with high-concurrency I/O-bound tasks (e.g., web scraping, database calls, API requests).
- Use threading when interacting with blocking I/O libraries that don't support async.
- Use multiprocessing for CPU-intensive tasks (e.g., data processing, machine learning).

## 3. Creating and Running Async Functions

### Q3: What is the difference between `async def` and `await` in Python?

**Answer:**

- `async def` defines an asynchronous function (coroutine).
- `await` is used inside `async def` functions to pause execution until an awaited coroutine completes.

  ```python
  import asyncio

  async def say_hello():
      print("Hello")
      await asyncio.sleep(1) # Non-blocking delay
      print("World!")

  asyncio.run(say_hello()) # Runs the async function
  ```

Follow-up: Can you call an async function directly without await?

Answer:
No. Calling an async function without await returns a coroutine object, not the result.

    async def foo():
        return "Hello"

    print(foo()) # <coroutine object foo>
    print(await foo()) # Correct way

## 4. Concurrency with asyncio.gather() and asyncio.create_task()

### Q4: What's the difference between asyncio.gather() and asyncio.create_task()?

Answer:

- `asyncio.gather(*tasks)`: Runs multiple coroutines concurrently and waits for all to complete.
- `asyncio.create_task()`: Schedules a coroutine without waiting for it to finish.

  ```python
    async def task(name, delay):
        await asyncio.sleep(delay)
        return f"{name} done"

        async def main():
        results = await asyncio.gather(task("Task 1", 2), task("Task 2", 3))
        print(results)

    asyncio.run(main()) # Waits for all tasks
  ```

Follow-up: Which one would you use if some tasks might fail and you want to handle errors individually?

Answer:

- Use `asyncio.create_task()` with try/except to handle errors separately.

```python
async def main():
    task1 = asyncio.create_task(task("Task 1", 2))
    task2 = asyncio.create_task(task("Task 2", 3))

    try:
        print(await task1)
    except Exception as e:
        print(f"Task 1 failed: {e}")

    try:
        print(await task2)
    except Exception as e:
        print(f"Task 2 failed: {e}")

asyncio.run(main())
```

## 5. Handling Blocking Code in Async Applications

### Q5: How do you run blocking operations (e.g., database queries, CPU-intensive tasks) in an async function?

Answer:

- Use `asyncio.to_thread()` for blocking I/O functions or `asyncio.run_in_executor()` for CPU-bound work.

```python
import asyncio
import time

def blocking_task():
    time.sleep(5)
    return "Done"

async def main():
    result = await asyncio.to_thread(blocking_task) # Runs in a separate thread
    print(result)

asyncio.run(main())
```

Follow-up: What happens if you call `time.sleep(5)` inside an async function?

Answer:
It blocks the entire event loop, causing performance issues. Use `await asyncio.sleep(5)` instead.

## 6. Exception Handling in Async Code

### Q6: How do you handle exceptions in asyncio tasks?

Answer:

- Wrap tasks in try/except or use `asyncio.gather()` with `return_exceptions=True`.

```python
async def faulty_task():
    raise ValueError("Something went wrong")

async def main():
    result = await asyncio.gather(faulty_task(), return_exceptions=True)
    print(result) # Prints the exception instead of crashing

asyncio.run(main())
```

## 7. Async Database Operations

### Q7: How would you integrate an async database client in a web application?

Answer:

- Use an async database driver like asyncpg (PostgreSQL) or TortoiseORM.
  Example with asyncpg:

```python
import asyncpg
import asyncio

async def fetch_data():
    conn = await asyncpg.connect("postgres://user:password@localhost/dbname")
    result = await conn.fetch("SELECT * FROM users")
    await conn.close()
    return result

asyncio.run(fetch_data())
```

## 8. Async HTTP Requests & WebSockets

### Q8: How do you make asynchronous HTTP requests in Python?

Answer:

- Use aiohttp instead of requests.

```python
import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

asyncio.run(fetch("https://example.com"))
```

## 9. Writing an Async Context Manager

### Q9: How do you implement an async context manager in Python?

**Answer:**

- Use async with and `__aenter__()`/`__aexit__()`.

```python
class AsyncFile:
    def __init__(self, filename):
        self.filename = filename

    async def __aenter__(self):
        self.file = await asyncio.to_thread(open, self.filename, "w")
        return self.file

    async def __aexit__(self, exc_type, exc, tb):
        await asyncio.to_thread(self.file.close)

async def main():
    async with AsyncFile("test.txt") as f:
        await asyncio.to_thread(f.write, "Hello")

asyncio.run(main())
```

## 10. Performance Optimization & Debugging

### Q10: How would you debug performance issues in an async Python application?

Answer:

- Use `asyncio.all_tasks()` to check running tasks.
- Use `aiomonitor` for real-time monitoring.
- Use `asyncio.run(debug=True)` for debug mode.
- Use `cProfile` or `yappi` to profile async code.
