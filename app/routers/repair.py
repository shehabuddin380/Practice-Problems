from fastapi import APIRouter, Body
from app.schemas.repair import RepairBooking

router = APIRouter(prefix="/repairs", tags=["Repairs"])


@router.post("", response_model=RepairBooking)
def create_repair(booking: RepairBooking):
    return booking


@router.post("/embedded", response_model=RepairBooking)
def create_embedded(booking: RepairBooking = Body(..., embed=True)):
    return booking
