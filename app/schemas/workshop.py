from pydantic import BaseModel


class Workshop(BaseModel):
    id: int
    name: str
    location: str


class WorkshopCreate(BaseModel):
    name: str
    location: str


class Instructor(BaseModel):
    id: int
    name: str
