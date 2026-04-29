def test(func):
    print("Before")
    func()
    print("After")

def greet():
    print("Hello")
def grant():
    print("Permission granted")

test(greet)
test(grant)


def test2(fun):
    def inner_test2():
        print("Before")
        fun()
        print("After")
    return inner_test2

greet = test2(greet)
greet()
print(greet.__name__)


def test3(fun):
    def inner_test3():
        print("Before")
        fun()
        print("After")
    return inner_test3

@test3
def new_greet():
    print("Hello there")
new_greet()
print(new_greet.__name__)


from functools import wraps
def test4(fun):
    @wraps(fun)
    def inner_test4():
        print("Before")
        fun()
        print("After")
    return inner_test4

@test4
def new_greet():
    print("Hello there")
new_greet()
print(new_greet.__name__)