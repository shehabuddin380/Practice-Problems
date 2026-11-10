from fastapi import FastAPI

from app.routers import (
    pantry,
    cafe,
    repairs,
    accounts,
    deliveries,
    workshops,
    rentals,
)

app = FastAPI(
    title="Class 03 Practice Problems",
    description="10 scenario-based FastAPI",
    version="1.0.0",
)

app.include_router(pantry.router)
app.include_router(cafe.router)
app.include_router(repairs.router)
app.include_router(accounts.router)
app.include_router(deliveries.router)
app.include_router(workshops.router)
app.include_router(rentals.router)


@app.get("/")
def root():
    return {"message": "Class 03 Practice Problems API is running"}
