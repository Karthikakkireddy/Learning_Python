class Car:
    type_ = "engine"
    
hyndai = Car()
print(hyndai.type_)

class Bat:
    pass
class Ball:
    pass

grey_nicols = Bat()
print(type(grey_nicols))
print(grey_nicols is Bat)
print(type(grey_nicols) is Bat)
print(type(grey_nicols) is Ball)
