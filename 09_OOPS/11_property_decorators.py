
class TeaLeaf:
    def __init__(self, age):
        self._age = age 

    @property
    def age(self):
        return self._age + 2

    @age.getter
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea leaf age must be between 1 and 5 years")
        
leaf_obj = TeaLeaf(2)
print(leaf_obj.age)
leaf_obj.age = 4
print(leaf_obj.age)