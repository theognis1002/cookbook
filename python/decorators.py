import time
"""
normal decorator - w no arguments
"""


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func()
        end = time.time()
        print("total time:", end-start)
        return rv
    return wrapper

@timer
def hello_world():
    print("hello world!")

hello_world()
# output:
# >>> hello world!
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