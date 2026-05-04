class A:
    property_a = "A : HELLO"
    def show_a(self):
        print("showing from A")

class B(A):
    property_b = "B : HI"
    def show_b(self):
        print("showing from B")

b_obj = B()
print(f"Property A from B object : {b_obj.property_a}")
print(f"Property A from B object : {b_obj.property_b}")