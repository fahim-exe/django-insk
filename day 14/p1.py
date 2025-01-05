#python function recap > without python methods

def greet(value):
    if isinstance(value, int):
        value = value+10
        return value
    
    if isinstance(value, str):
        value = "Hi"+ value
        return value
    
    return"You type doesnot support"


print(greet(10))

print(greet("fahim"))

print(greet({"name":"fahim"}))