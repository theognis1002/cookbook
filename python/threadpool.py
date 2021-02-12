import concurrent.futures
import random


def my_function(num):
    return num ** 2


with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:

    futures = []
    for _ in range(99):
        futures.append(executor.submit(my_function, random.randint(1, 99)))

    results = []
    for future in concurrent.futures.as_completed(futures):
        results.append(future.result())

    print(results)