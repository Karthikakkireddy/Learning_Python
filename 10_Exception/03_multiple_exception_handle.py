

def check_order(item, quantity):
    try:
        price = {"masala" : 20 }[item]
        if isinstance(quantity, str):
            raise TypeError
        cost = price * quantity
        print(f"Total cost is {cost}")
       
    except KeyError:
        print("Sorry this item is not available in menu")
    except TypeError:
        print("Quantity cannot be string")

check_order("ginger", 2)
check_order("masala", "two")
check_order("masala", 2)