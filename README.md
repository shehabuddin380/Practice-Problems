# Class 03 Practice Problems — FastAPI + Pydantic v2

## Project structure

```text
class03_fastapi_project/
├── main.py
├── requirements.txt
├── README.md
├── app/
│   ├── __init__.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── pantry.py
│   │   ├── cafe.py
│   │   ├── repair.py
│   │   ├── account.py
│   │   ├── delivery.py
│   │   ├── workshop.py
│   │   ├── rental.py
│   │   ├── checkin.py
│   │   ├── notification.py
│   │   └── event.py
│   └── routers/
│       ├── __init__.py
│       ├── pantry.py
│       ├── cafe.py
│       ├── repairs.py
│       ├── accounts.py
│       ├── deliveries.py
│       ├── workshops.py
│       ├── instructors.py
│       ├── rentals.py
│       ├── checkins.py
│       ├── notifications.py
│       └── events.py
└── tests/
    └── test_api.py
```

## Run

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload
```

Swagger UI: `http://127.0.0.1:8000/docs`

## Ten exercises

1. Smart Pantry Inventory
2. Cafe Menu Search & Filtering
3. Repair Booking with Nested Address
4. Account Signup Normalizer
5. Delivery Tracking: Path, Query & Route Order
6. Workshop API with APIRouter
7. Equipment Rental: Input vs Output Models
8. Staff Access: Discriminated Union
9. Generic Notification Feed & Recursive Categories
10. Event Registration: Strict vs Lax + Serialization

All data is kept in memory. No database is required.
