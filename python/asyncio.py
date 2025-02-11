import asyncio
import time

import aiohttp

start_time = time.time()


async def make_request(session, url):
    response = await session.get(url)
    return await response.json()


async def main():

    async with aiohttp.ClientSession() as session:
        tasks = [make_request(session, "https://httpbin.org/ip") for _ in range(9)]
        result = await asyncio.gather(*tasks)
        print(result)

    """
    NOTE:
    asyncio.gather is a way to run multiple tasks concurrently and wait for all of them to complete.
    It's like Promise.all in JavaScript.
    asyncio.create_task is a way to run a task concurrently and return a task object. It doesn't wait for the task to complete.
    """


if __name__ == "__main__":
    asyncio.run(main())
    print("--- %s seconds ---" % (time.time() - start_time))
