
users = []

def get_input():
    user = input("Enter your name : ")
    return user

def validate_input():    
    print("Validation is successful")

def save_to_db(user):
    users.append(user)

def register_user():
    user = get_input()
    validate_input()
    save_to_db(user)
    print(f"User - {user} , registered successfully ")

register_user()