"""
Custom context manager
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
