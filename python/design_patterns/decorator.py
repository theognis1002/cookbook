from functools import wraps

"""
Best practice: use functools wraps
    - Without the use of this decorator factory, the name of example_func would have been 'with_logging', and the docstring of the original example_func() would have been lost.
"""


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


if __name__ == "__main__":
    print(example_func.__name__)  # prints 'example_func'
    print(example_func.__doc__)  # prints 'does some math'
    print(
        example_func(3)
    )  # prints return value and extra decorator functionality "example_func was called"
