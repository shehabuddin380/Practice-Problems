from fastapi import APIRouter, HTTPException
from app.schemas.rental import RentalDB, RentalIn, RentalOut

router = APIRouter(prefix="/rentals", tags=["Rentals"])
rental_db: dict[int, RentalDB] = {
    1: RentalDB(
        id=1,
        equipment_name="Projector",
        rental_days=3,
        renter_email="customer@example.com",
        access_code="SECRET-123",
    )
}


@router.get("/summary", response_model=list[RentalOut])
def rental_summary():
    return list(rental_db.values())


@router.get("/{rental_id}", response_model=RentalOut)
def get_rental(rental_id: int):
    if rental_id not in rental_db:
        raise HTTPException(status_code=404, detail="Rental not found")
    return rental_db[rental_id]


@router.post("", response_model=RentalOut)
def create_rental(rental: RentalIn):
    new_id = max(rental_db.keys(), default=0) + 1
    record = RentalDB(
        id=new_id,
        equipment_name=rental.equipment_name,
        rental_days=rental.rental_days,
        renter_email=rental.renter_email,
        access_code="TEMP-ACCESS",
    )
    rental_db[new_id] = record
    return record
