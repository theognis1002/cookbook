"""
1. override __new__ method (which is called before __init__) to get or create a class instance
1. add state to track if already initialized in __init__ method - this is only needed if the __init__ method has a side effect.
"""
class Singleton(object):
    _instance = None
    _inited = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, *args, **kwargs):
        if type(self)._inited:  # only necessary if there is a side effect in the __init__method (ie; self.x = 1)
            return
        self.x = 1
        type(self)._inited = True
    
    def increment_thing(self):
        self.x += 1

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    if id(s1) == id(s2):
        print("Same instance")
    else:
        print("Different instance")
