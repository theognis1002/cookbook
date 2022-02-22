import dataclasses
import inspect
from dataclasses import dataclass, field
from pprint import pprint
from typing import List
import attr


@dataclass
class Employee:
    name: str
    role: str
    vacation_days: int = 25


e = Employee(name="Joe", role="admin")
print(e)

# output:
# Employee(name="Joe", role="admin", vacation_days=25)

"""
above example is equivalent of the following:
"""


class Employee:
    def __init__(self, name, role, vacation_days=25):
        self.name = name
        self.role = role
        self.vacation_days = vacation_days

    def __repr__(self):
        return f"{type(self).__name__}(name='{self.name}', role='{self.role}', vacation_days={self.vacation_days})"


e = Employee(name="Joe", role="admin")
print(e)

# output:
# Employee(name="Joe", role="admin", vacation_days=25)


class ManualComment:
    def __init__(self, id: int, text: str):
        self.id: int = id
        self.text: str = text

    def __repr__(self):
        return "{}(id={}, text={})".format(self.__class__.__name__, self.id, self.text)

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) == (other.id, other.text)
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        else:
            return not result

    def __hash__(self):
        return hash((self.__class__, self.id, self.text))

    def __lt__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) < (other.id, other.text)
        else:
            return NotImplemented

    def __le__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) <= (other.id, other.text)
        else:
            return NotImplemented

    def __gt__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) > (other.id, other.text)
        else:
            return NotImplemented

    def __ge__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) >= (other.id, other.text)
        else:
            return NotImplemented


@dataclass(frozen=True, order=True)
class Comment:
    id: int
    text: str = ""
    replies: List[int] = field(default_factory=list, repr=False, compare=False)


@attr.s(frozen=True, order=True, slots=True)
class AttrComment:
    id: int = 0
    text: str = ""
