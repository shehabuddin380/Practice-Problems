from fastapi import APIRouter, HTTPException, status
from app.schemas.workshop import Workshop, WorkshopCreate

router = APIRouter(prefix="/workshops", tags=["Workshops"])
workshops = {
    1: Workshop(id=1, name="Auto Repair Lab", location="Dhaka"),
    2: Workshop(id=2, name="Electronics Lab", location="Chattogram"),
}


@router.get("/", response_model=list[Workshop])
def list_workshops():
    return list(workshops.values())


@router.get("/{workshop_id}", response_model=Workshop)
def get_workshop(workshop_id: int):
    if workshop_id not in workshops:
        raise HTTPException(status_code=404, detail="Workshop not found")
    return workshops[workshop_id]


@router.post("/", response_model=Workshop, status_code=status.HTTP_201_CREATED)
def create_workshop(workshop: WorkshopCreate):
    new_id = max(workshops.keys(), default=0) + 1
    record = Workshop(id=new_id, **workshop.model_dump())
    workshops[new_id] = record
    return record
