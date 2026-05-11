from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id : int 
    items : List[str]
    quantities : Dict[str, int ]

class BlogPost(BaseModel):
    title : str
    content : str
    image_url : Optional[str] = None

cart_data = {
    "user_id" : 123,
    "items" : ["Laptop", "Mouse", "Keyboard"],
    "quantities" : { "Laptop" : 110, "Mouse" : 55, "Keyboard" : 30}
}


cart_obj = Cart(**cart_data)
print(cart_obj)