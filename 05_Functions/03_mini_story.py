def caluculate_bills(cups, price_per_cup):
    return cups * price_per_cup

my_bill = caluculate_bills(3, 15)
print(f"My bill - {my_bill}")

print("Order for table 8:", caluculate_bills(2, 30))