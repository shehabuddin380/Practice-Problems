from fastapi import APIRouter, status
from app.schemas.account import AccountSignup, AccountResponse

router = APIRouter(prefix="/accounts", tags=["Accounts"])


@router.post("", response_model=AccountResponse, status_code=status.HTTP_201_CREATED)
def create_account(account: AccountSignup):
    return account
