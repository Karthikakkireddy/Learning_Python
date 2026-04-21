size_cup = input("Choose your size - \n Available Options -  (Small , Medium , Large ) - ").lower()


if(size_cup == 'small'):
    print(f"Your bill for size  {size_cup } : 10 rupees")

elif size_cup == 'medium':
    print(f"Your bill for size  {size_cup} : 15 rupees")

elif size_cup == 'large':
    print(f"Your bill for size  {size_cup} : 20 rupees")
else:
    print(f"Unknown cup size")

