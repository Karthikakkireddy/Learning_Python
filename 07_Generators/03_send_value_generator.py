def gen():
    print("Hello Welcome")
    x = yield "You need to send the value"
    while True:
        print(f"Preparing: {x}")
        x = yield f"You need to send the value : Current value {x}"


g =gen()
next(g)
g.send(10)
g.send(20)

def exp():
    x = yield "YOU NEED TO SEND THE VALUE"
    print(f"Value : {x}")
temp = exp()
print(next(temp))
# temp.send(10) # StopIteration Error
try:
    temp.send(10)
except StopIteration:
    pass


def gen2():
    print("Hello Welcome")
    x = yield "You need to send the value"
    while True:
        print(f"Preparing: {x}")
        x = yield f"You need to send the value : Current value {x}"


g2 =gen2()
print(next(g2))
print(g2.send(10))
print(g2.send(20))
