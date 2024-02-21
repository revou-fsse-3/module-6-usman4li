from typing import Optional
from pydantic import BaseModel, Field

class Update_employees_request(BaseModel):
    name: str = Field(... , description="Employees name", min_length=3, max_length=50)
    age: Optional[int] = Field(None, description="Employees age")
    gender:str = Field(... , description="Employees gender", min_length=3, max_length=50)
    job: str = Field(... , description="Employees habitat", min_length=3, max_length=50)