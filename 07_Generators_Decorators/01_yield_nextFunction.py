
def gen():
    print("Hello")
    yield 1
    print("Hello 2")
    yield 2
    print("Hello 3")
    yield 3
    print("Bye")



temp = gen()
print(next(temp))
print(next(temp))
print(next(temp))

