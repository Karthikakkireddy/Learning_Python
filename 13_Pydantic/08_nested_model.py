from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street  : str
    city : str
    postal_code : str

class User(BaseModel):
    id : int 
    name : str
    address : Address 


address = Address(
    street= "93048210934590345", 
    city="Hyderabad",
    postal_code="500000"
)

user1 = User (
    id="1001",
    name = "Karthik",
    address= address
)

print(user1)

user_data_2 = {
    "id" : 1001,
    "name": "Aditya",
    "address":{
        "street" : "123 anything",
        "city" : "Hyderabad",
        "postal_code" : "23442354"
    }
}

user2 = User(**user_data_2)
print(user2)