import functools

"""
Best practice: use functools wraps
    - Without the use of this decorator factory, the name of example_func would have been 'with_logging', and the docstring of the original example_func() would have been lost.
"""


def logged(func):
    @functools.wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logged
def example_func(x):
    """does some math"""
    return x + x * x


if __name__ == "__main__":
    print(example_func.__name__)  # prints 'example_func'
    print(example_func.__doc__)  # prints 'does some math'
    print(
        example_func(3)
    )  # prints return value and extra decorator functionality "example_func was called"


"""
cache decorator - func & class implementation
"""


def cached(func):
    cached_data = {}

    @functools.wraps(func)
    def cached_dec(*args):
        try:
            return cached_data[args]
        except KeyError:
            cached_data[args] = ret = func(*args)
            return ret
        return cached_dec


class cached:
    def __init__(self, func):
        self.func = func
        self.cached_data = {}

        functools.update_wrapper(self, func)

    def __call__(self, *args):
        try:
            return self.cached_data[args]
        except KeyError:
            self.cached_data[args] = ret = self.func(*args)
            return ret


@cached
def compute(x: int) -> int:
    print(f"calling w/ {x}")
    return x * x
