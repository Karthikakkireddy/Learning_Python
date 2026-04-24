names = ["Karthik", "aditya", "Neeraj"]
bill = [55, 60]

for name, amount in zip(names, bill):
    print(f"{name} paid ${amount}")