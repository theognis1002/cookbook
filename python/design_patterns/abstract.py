from abc import ABC, abstractmethod

"""
    All classes that inherit from the AbstractBase (which inherits from the built-in ABC class) must override all methods decorated by @abstractmethod
"""


class AbstractBase(ABC):
    @abstractmethod
    def do_something(self):
        raise NotImplementedError

    @abstractmethod
    def print_something(self):
        raise NotImplementedError


class CustomClass(AbstractBase):
    def do_something(self, x, y):
        return x + y

    def print_something(self):
        print("Hello World!")


if __name__ == "__main__":
    obj = CustomClass()
    result = obj.do_something(3, 4)
    print(result)
