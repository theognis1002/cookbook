from dataclasses import dataclass


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
