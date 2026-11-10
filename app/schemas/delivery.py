from pydantic import BaseModel, Field


class Delivery(BaseModel):
    tracking_id: int = Field(ge=1000, le=99999)
    status: str
