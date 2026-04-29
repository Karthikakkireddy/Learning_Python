from functools import wraps

def log_activity(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("Before calling : ",func.__name__)
        func(*args, **kwargs)
        print("After calling : ",func.__name__)
    return inner

@log_activity
def brew_chai(chai_type):
    print(f"Brewing {chai_type}")

brew_chai("Masala Chai")


# PROBLEM - If the function gives a return type we need to make sure that wrapper/inner function also does that


def log_activity2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before calling : ",func.__name__)
        result= func(*args, **kwargs)
        print("After calling : ",func.__name__)
        return result
    return wrapper

@log_activity2
def add(a,b):
    return a+b

print(add(10,5))