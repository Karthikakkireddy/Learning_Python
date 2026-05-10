from pydantic import BaseModel

class User(BaseModel):
    id : int
    name : str
    is_active : bool 

input_data = {'id' : "101", 'name' : "Karthik", 'is_active' : True} 
input_data2 = {'id' : 101, 'name' : "Karthik", 'is_active' : True} 

user = User(**input_data)
user2 = User(**input_data2)

print(user)
print(user2)
