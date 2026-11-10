from pydantic import BaseModel, EmailStr, Field


class RentalIn(BaseModel):
    equipment_name: str
    renter_email: EmailStr
    rental_days: int = Field(ge=1, le=90)


class RentalOut(BaseModel):
    id: int
    equipment_name: str
    rental_days: int


class RentalDB(RentalOut):
    renter_email: EmailStr
    access_code: str
