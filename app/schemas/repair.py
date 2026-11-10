from datetime import datetime
from pydantic import BaseModel, Field


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class RepairBooking(BaseModel):
    customer_name: str
    appliance: str
    address: Address
    preferred_date: datetime
    issue_tags: list[str] = Field(default_factory=list)
