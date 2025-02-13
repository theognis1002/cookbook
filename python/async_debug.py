import asyncio
import tracemalloc

tracemalloc.start()


async def task():
    await asyncio.sleep(1)


asyncio.run(task())
print(tracemalloc.get_traced_memory())
