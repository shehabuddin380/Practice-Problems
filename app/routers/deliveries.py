from fastapi import APIRouter, HTTPException, Path, Query, status
from app.schemas.delivery import Delivery

router = APIRouter(prefix="/deliveries", tags=["Deliveries"])
delivery_db = {
    1001: {"tracking_id": 1001, "status": "in_transit"},
    1002: {"tracking_id": 1002, "status": "delivered"},
    1003: {"tracking_id": 1003, "status": "processing"},
}


@router.get("/recent", summary="List recent deliveries")
def recent():
    return list(delivery_db.values())


@router.get("", response_model=list[Delivery], summary="Filter deliveries")
def list_deliveries(
    status: str | None = Query(None),
    max_length: int = Query(20, ge=1, le=100),
    limit: int = Query(20, ge=1, le=100),
):
    results = list(delivery_db.values())
    if status:
        results = [item for item in results if item["status"].lower() == status.lower()]
    return results[: min(max_length, limit)]


@router.get("/{tracking_id}", response_model=Delivery, summary="Get one delivery by tracking ID")
def get_delivery(tracking_id: int = Path(..., ge=1000, le=99999)):
    if tracking_id not in delivery_db:
        raise HTTPException(status_code=404, detail="Delivery not found")
    return delivery_db[tracking_id]


@router.post("", response_model=Delivery, status_code=status.HTTP_201_CREATED, summary="Create a delivery")
def create_delivery(delivery: Delivery):
    delivery_db[delivery.tracking_id] = delivery.model_dump()
    return delivery
