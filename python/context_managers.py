"""
Custom context manager
"""
"""
#1) contextlib
"""
from contextlib import contextmanager


def acquire_resource(*args, **kwargs):
    """setup function"""
    pass


def release_resource(*args, **kwargs):
    """teardown function"""
    pass


@contextmanager  # builtin decorator
def managed_resource(*args, **kwds):
    # Code to acquire resource, e.g.:
    resource = acquire_resource(*args, **kwds)
    try:
        yield resource
    finally:
        # Code to release resource, e.g.:
        release_resource(resource)


with managed_resource(timeout=3600) as resource:
    pass
    # Resource is released at the end of this block,
    # even if code in the block raises an exception

"""
#2) Class-Based
"""


class FileHandler:
    def __init__(self, file_name, file_mode):
        self._file_name = file_name
        self._file_mode = file_mode

    def __enter__(self):
        self._file = open(self._file_name, self._file_mode)
        return self._file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self._file.close()


with FileHandler("test.txt", "w") as f:
    f.write("Test")


"""
#3) Decorator
"""
from contextlib import ContextDecorator


class file_handler_mixin(ContextDecorator):
    def __init__(self, file_name, file_mode):
        self._file_name = file_name
        self._file_mode = file_mode
        self._file = None

    def __enter__(self):
        print(f"Enter Method: File Name {self._file_name}")
        self._file = open(self._file_name, self._file_mode)
        return self._file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(f"Exit Method: File Mode {self._file_mode}")
        self._file.close()


@file_handler_mixin("test.txt", "w")
def write_to_file():
    print("Not access to the value returned by the __enter__ method")


if __name__ == "__main__":
    write_to_file()
