from typing import Optional
from pydantic import BaseModel, Field

class Update_animals_request(BaseModel):
    species: str = Field(... , description="Animals species", min_length=3, max_length=50)
    age: Optional[int] = Field(None, description="Animals age")
    gender:str = Field(... , description="Animals gender", min_length=3, max_length=50)
    habitat: str = Field(... , description="Animals habitat", min_length=3, max_length=50)
    countries: str = Field(... , description="Animals countries", min_length=3, max_length=50)