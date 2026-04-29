from functools import wraps

def authenticator(func):
    @wraps(func)
    def wrapper(user_type):
        if user_type == "admin":
            return func(user_type)
        else:
            print(f"You are {user_type}, only admins are allowed")
            return None # Optional but Fail proof - You might see this in older code bases
    return wrapper

@authenticator
def log_in(user_role):
    print("Log in as admin is successful")

log_in("user")
log_in("admin")