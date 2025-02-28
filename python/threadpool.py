import concurrent.futures

import requests


def crawl_page(url):
    response = requests.get(url)
    print(response.status_code, url)
    return response.json()


with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(
        crawl_page,
        [f"https://jsonplaceholder.typicode.com/posts/{i}" for i in range(1, 100)],
    )
    for result in results:
        print(result)
