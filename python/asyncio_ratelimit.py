import asyncio
import time

import aiohttp
from aiolimiter import AsyncLimiter

limiter = AsyncLimiter(3, 1)
ref = time.time()


async def task(id):
    await asyncio.sleep(id * 0.01)
    async with limiter:
        async with aiohttp.ClientSession() as session:
            headers = {"User-Agent": "foo"}
            async with session.get(
                "http://httpbin.org/user-agent", headers=headers
            ) as response:

                print("Status:", await response.json())
                print(f"{id:>2d}: Drip! {time.time() - ref:>5.2f}")
                print("*" * 55)


tasks = [task(i) for i in range(9999)]


start = time.time()
result = asyncio.run(asyncio.wait(tasks))

print(time.time() - start)
