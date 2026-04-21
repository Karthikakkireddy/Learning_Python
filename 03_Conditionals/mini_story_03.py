size_cup = input("Choose your size - \n Available Options - Small , Medium , Large : ").lower()
price

if(size_cup == 'small'):
    price = 10
if size_cup == 'medium':
    price = 15
if size_cup == 'large':
    price = 20

print(f"Your bill is : {price} for size : {size_cup}")