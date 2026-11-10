from pydantic import BaseModel, Field


class MenuItem(BaseModel):
    title: str = Field(min_length=2, max_length=60)
    price: float = Field(gt=0, le=2500)
    available: bool
    cuisine: str
