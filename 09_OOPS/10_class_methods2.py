class A:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll


    @classmethod
    def from_dict(cls, dict_info):
        return cls(
            dict_info["name"], 
            dict_info["roll"]
        )
    
    @classmethod
    def from_string(cls, string_info):
        name , roll = string_info.split("-")

        return cls(name, roll)
    
student1 = A.from_dict({"name":"Kartik", "roll":6225})

student2 = A.from_string("Aditya-6628")

# print(student1) <__main__.A object at 0x1011446e0>
# print(student2) <__main__.A object at 0x101130550>

print(student1.__dict__)
print(student2.__dict__)


student3 = A("Neeraj", 6633)
print(student3.__dict__)