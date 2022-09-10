### https://alexmarandon.com/articles/python_mock_gotchas/

# decorators.py
# decorators.py
def noise_logger(func):
    def wrapped(self):
        result = func(self)
        # In a real-world scenario, the decorator would access an external
        # resource which we don't want our tests to depend on, such as a
        # caching service.
        print("Pet made noise: ", result)
        return result

    return wrapped


# person.py
from decorators import noise_logger


class Person(object):
    def __init__(self):
        self.pet = Pet()


class Pet(object):
    @noise_logger
    def noise(self):
        return "Woof"


# tests.py
from mock import patch
from person import Person


@patch("person.noise_logger", lambda x: x)
def test_decorator():
    person = Person()
    assert person.pet.noise() == "Woof"


"""
Unfortunately this won’t work at all because by the time we patch our decorator, it has already been applied and our noise method has already been wrapped.
"""

"""
SOLUTION:
To deal with this you first have to make sure that your decorator is defined in a module separate from the class, otherwise you’ll never get a chance to replace it with a mock before the class definition calls it. Then you need to write your test code so that it patches the decorator before it gets applied to the methods of your class:
"""
# tests.py
from mock import patch

patch("decorators.noise_logger", lambda x: x).start()
from person import Person


def test_decorator():
    person = Person()
    assert person.pet.noise() == "Woof"
