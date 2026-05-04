class A:
    def show(self):
        print("In A show")

class B:
    def show(self):
        print("In B show")

class C(A,B):
    pass

class D(B,A):
    pass

c_obj = C()
d_obj = D()
c_obj.show()
d_obj.show()