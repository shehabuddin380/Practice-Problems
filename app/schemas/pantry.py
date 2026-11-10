from datetime import datetime
from pydantic import BaseModel, Field


class PantryItem(BaseModel):
    name: str = Field(min_length=2, max_length=40)
    quantity: int = Field(ge=0, le=500)
    category: str
    sku: str = Field(pattern=r"^PAN-\d{4}$")
    expiry_date: datetime


class PantryResponse(PantryItem):
    id: int
