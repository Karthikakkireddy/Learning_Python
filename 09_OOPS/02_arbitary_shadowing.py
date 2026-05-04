class Chai:
    temperature = "hot"
    strength = "strong"

chai_obj = Chai()

print(chai_obj.strength)
print(chai_obj.temperature)
chai_obj.strength = "mild"

chai_obj2 = Chai()
print("Chai Obj 1 ", chai_obj.strength)
print("Chai Obj 2 ", chai_obj2.strength)

del chai_obj.strength

print("Chai Obj 1 (After deleting strength) ", chai_obj.strength)