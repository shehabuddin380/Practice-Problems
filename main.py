from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Class 03 Practice API",
    description="10 scenario-based FastAPI and Pydantic practice exercises",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "FastAPI Class 03 API is running"
    }