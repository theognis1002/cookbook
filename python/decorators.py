import time

"""
normal decorator - w no arguments
"""


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func()
        end = time.time()
        print("total time:", end - start)
        return rv

    return wrapper


@timer
def compute():
    print("result:", 2 * 2)


compute()
# output:
# >>> result: 4
# >>> total time: 0.0001


"""
decorators with arguments - have a function with the input argument that returns a 'normal' decorator
"""


def repeat(argument):
    def decorator(function):
        def wrapper(*args, **kwargs):
            for _ in range(argument):
                result = function(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(3)
def hello_world():
    print("hello world!")


hello_world()
# output:
# >>> hello world!
# >>> hello world!
# >>> hello world!

def dec_with_args(*args, **kwargs):
    def _dec_with_args(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
        return wrapper

    if len(args) == 1 and callable(args[0]):
        # No arguments, this is the decorator
        # Set default values for the arguments
        return _dec_with_args(args[0])
    else:
        # This is just returning the decorator
        return _dec_with_args


@dec_with_args("my_arg")
def test():
    print("my func")

"""
'stateful' decorators - keeps 'state' in memory between function calls. takes advantage of the fact that the outer function only runs once when we decorate the function
"""


def once_per_minute(
    func,
):  # outer function only runs once when we decorate the function
    last_invoked = 0

    def wrapper(
        *args, **kwargs
    ):  # wrapper and inner function are called each time the function is called
        nonlocal last_invoked  # increment last_invoked var which is in outer scope
        elapsed_time = time.time() - last_invoked

        if elapsed_time < 60:
            raise Exception(f"Only {elapsed_time} has passed. Please wait.")

        last_invoked = time.time()
        return func(*args, **kwargs)

    return wrapper


@once_per_minute
def dummy_api_call():
    time.sleep(1)
    print("data!")


dummy_api_call()
dummy_api_call()

# output:
# data!
# Traceback (most recent call last):
# ...
#    raise Exception(f"Only {elapsed_time} has passed. Please wait.")
# Exception: Only 1.0012216567993164 has passed. Please wait

"""
additional 'stateful' decorator - custom implementation of memoize
"""


def memoize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        if args not in cache:
            print(f"Caching NEW value for {func.__name__}{args}")
            cache[args] = func(*args, **kwargs)
        else:
            print(f"Using OLD value for {func.__name__}{args}")
        return cache[args]

    return wrapper


@memoize
def compute(x, y):
    return x ** y


result = compute(3, 4)
print(result)
result = compute(3, 4)
print(result)

# output:
# >>> Caching NEW value for compute(3, 4)
# >>> 81
# >>> Using OLD value for compute(3, 4)
# >>> 81
