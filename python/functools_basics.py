import functools

"""
@functools.lru_cache - Memoization - Least Recently Used
"""

i = 0
def check_function_ran():
    global i
    i += 1
    print(f"Function ran {i} times!")


@functools.lru_cache(maxsize=3)
def count_vowels(sentence):
    sentence = sentence.casefold()
    check_function_ran()  # print output if 'count_vowels' function was ran and cache was not used
    return sum(sentence.count(vowel) for vowel in 'aeiou')


for _ in range(9):
    result = count_vowels('hello world')
    print(result)


"""
@functools.wraps - Without the use of this decorator factory, the name of example_func would have been 'with_logging', and the docstring of the original example_func() would have been lost.
"""
from functools import wraps


def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logged
def example_func(x):
    """does some math"""
    return x + x * x


print(example_func.__name__)  # prints 'example_func'
print(example_func.__doc__)  # prints 'does some math'
print(
    example_func(3)
)  # prints return value and extra decorator functionality "example_func was called"

