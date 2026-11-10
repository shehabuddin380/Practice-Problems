from fastapi import APIRouter, Query
from app.schemas.cafe import MenuItem

router = APIRouter(prefix="/menu", tags=["Cafe Menu"])
menu_db = [
    MenuItem(title="Chicken Burger", price=450, available=True, cuisine="Bangladeshi"),
    MenuItem(title="Beef Steak", price=1200, available=True, cuisine="Continental"),
    MenuItem(title="Pasta Alfredo", price=650, available=True, cuisine="Italian"),
    MenuItem(title="Chicken Biryani", price=380, available=False, cuisine="Bangladeshi"),
    MenuItem(title="Margherita Pizza", price=700, available=True, cuisine="Italian"),
    MenuItem(title="Sushi Roll", price=950, available=True, cuisine="Japanese"),
]


@router.get("", response_model=list[MenuItem])
def search_menu(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=50),
    cuisine: str | None = Query(None, min_length=2, max_length=30),
    min_price: float | None = Query(None, ge=0),
):
    results = menu_db
    if cuisine is not None:
        results = [item for item in results if item.cuisine.lower() == cuisine.lower()]
    if min_price is not None:
        results = [item for item in results if item.price >= min_price]
    return results[skip: skip + limit]
