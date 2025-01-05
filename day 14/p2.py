#python function recap > with python methods

from functools import singledispatch


@singledispatch
def greet(value):
    return"You type doesnot support"

@greet.register(int)
def handle_int(value):
    return value+10

@greet.register(str)
def handle_str(value):
    return f"Hi {value}"


print(greet(10))
print(greet("fahim"))
print(greet([1,2,3]))