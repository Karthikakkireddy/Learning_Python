class A:
    property_a = "Hi"
    def show(self):
        return f"From property A : {self.property_a}"

obj_a = A()
print( obj_a.show() )


class B:
    property_b = "Hi"
    @staticmethod
    def show():
        return f"From property B : {B.property_b}"

obj_b = B.show()
print( obj_b )


# CLass methods
class C:
    property_c = "Hello"
    @classmethod
    def show(cls):
        return f"From property C : {cls.property_c}"

class D(C):
    property_c = "HI"
print( C.show() )
print( D.show() )