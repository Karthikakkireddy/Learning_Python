
snack = input("Enter your snack choice: ").lower()

if (snack == "samosa" or snack == "cookie"):
    print(f"Order confirmed : {snack}")
else:
    print(f"Order is unavailable : {snack}")
    
