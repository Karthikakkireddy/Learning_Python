class A:
    def __init__(self):
        print("In A init")

class B(A): 
    pass

class C(A):
    def __init__(self):
        print("In C init")


class D():
    def __init__(self):
        print("In D init")
 
# class E(A,C): gives Errror 
#     pass

class E(A,D):
    pass
class F(D,A):
    pass

b_obj = B()
c_obj = C()
e_obj = E()
f_obj = F()