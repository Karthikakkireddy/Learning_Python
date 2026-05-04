class Chaicup:
    sales =150
    def describe(self):
        return f"A {self.sales} ml cup of chai"

cup = Chaicup()
print(cup.describe())

# print(Chaicup.describe()) -- Attribute error 
# print(Chaicup.describe(Chaicup())) -- You need to pass an object of type Chaicup()

cup_two = Chaicup()
print(cup_two.describe())