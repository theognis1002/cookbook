from typing import TypedDict


class User(TypedDict):
    id: int
    name: str
    age: int


user: User = {"id": 1, "name": "John", "age": 30}

print(user)
