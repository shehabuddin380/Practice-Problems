from fastapi import APIRouter, HTTPException, status
from app.schemas.pantry import PantryItem, PantryResponse

router = APIRouter(prefix="/pantry", tags=["Pantry"])
pantry_db: dict[int, dict] = {}
next_id = 1


@router.post("", response_model=PantryResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: PantryItem):
    global next_id
    record = item.model_dump()
    record["id"] = next_id
    record["supplier_cost"] = 125.50
    pantry_db[next_id] = record
    next_id += 1
    return record


@router.get("/{item_id}", response_model=PantryResponse)
def get_item(item_id: int):
    if item_id not in pantry_db:
        raise HTTPException(status_code=404, detail="Pantry item not found")
    return pantry_db[item_id]


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    if item_id not in pantry_db:
        raise HTTPException(status_code=404, detail="Pantry item not found")
    del pantry_db[item_id]
    return None
