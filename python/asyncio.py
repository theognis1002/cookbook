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


if __name__ == "__main__":
    asyncio.run(main())
    print("--- %s seconds ---" % (time.time() - start_time))
