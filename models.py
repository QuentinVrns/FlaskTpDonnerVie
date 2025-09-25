from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Supplier(BaseModel):
    id: Optional[int] = Field(default=None)
    name: str = Field(min_length=2, max_length=100)
    address: str = Field(min_length=5, max_length=255)
    email: EmailStr
    phone: str = Field(min_length=6, max_length=30)
