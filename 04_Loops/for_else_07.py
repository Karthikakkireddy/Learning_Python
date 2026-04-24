

staff = [("Karthik", 16),("Deepak", 17) ,( "Surya", 17) ,("Aditya", 17), ("Neeraj", 15)]

for name,age in staff:
    if age < 18:
        print(f"{name} is eligilble to work")
        break
else:
    print("No one is eligible to work")