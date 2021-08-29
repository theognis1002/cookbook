import asyncio
import random
import time

import aiohttp
from utils.proxies import proxies

start_time = time.time()


def sync_func():
    time.sleep(5)
    print("sync_func ran")


async def make_request(session, url):
    response = await session.get(url)
    return await response.json()


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [make_request(session, "https://httpbin.org/ip") for _ in range(99)]
        result = await asyncio.gather(*tasks)
        print(result)


if __name__ == "__main__":
    sync_func()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    sync_func()

    loop.close()
    print("--- %s seconds ---" % (time.time() - start_time))
