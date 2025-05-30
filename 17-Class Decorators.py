import types

def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = types.MethodType(greet, cls)
    return cls


