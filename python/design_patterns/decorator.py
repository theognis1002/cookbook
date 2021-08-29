from functools import wraps


def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logged
def f(x):
    """does some math"""
    return x + x * x


if __name__ == "__main__":
    print(f.__name__)  # prints 'f'
    print(f.__doc__)  # prints 'does some math'
    print(f(3))  # prints return value and extra decorator functionality "f was called"
