def gen():
    print("Hello Welcome")
    x = yield 
    while True:
        print(f"Preparing: {x}")
        x = yield 


g =gen()
next(g)
g.send(10)
g.send(20)