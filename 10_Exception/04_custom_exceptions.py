class OutOfIngridientsError(Exception):
    pass

def make_tea(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngridientsError("Missing milk or sugar")
    print("Tea is ready")

try:
    make_tea(0,1)
except OutOfIngridientsError as e:
    print(f"Error : ", e)

    
make_tea(0,1)