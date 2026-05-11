from typing import Optional
from pydantic import BaseModel, Field

class Employee:
    name : str = Field(
        ..., # Means this is required field
        min_length = 3,
        max_length = 50, 
        description = "Employee Name", # Description and examples are useful for documentation
        examples= "Karthik Akkireddy"
    )

    department : Optional[str] = 'General'
    salary : float = Field( 
        ...,
        ge = 1000 # ge = Greater than or equal to ; gt = greater than
    )