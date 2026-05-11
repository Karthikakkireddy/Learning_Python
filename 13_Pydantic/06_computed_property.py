from pydantic import BaseModel, computed_field, Field

class Product(BaseModel):
    price: float 
    quantity: int

    #Goal : calculate the total price with a given price and quantity we can do it directly in here rather than in controller or logic
    @computed_field
    @property #Makes it accessible as an attribute/field
    def total_price(self) -> float : # -> float : means the return type have to be float
        return self.price * self.quantity
    

class Booking(BaseModel):
    user_id : int
    room_id : int
    nights : int = Field(
        ...,
        ge=1 
    )
    rate_per_night : float

    @computed_field
    @property
    def total_amount(self ) -> float : 
        return self.nights * self.rate_per_night
    
booking = Booking(
    user_id=123,
    room_id=456,
    nights = 3,
    rate_per_night=100.0
)

print(booking.total_amount)
print(booking.model_dump())