from pydantic import BaseModel, field_validator, model_validator


class AccountSignup(BaseModel):
    email: str
    password: str
    confirm_password: str
    display_name: str

    @field_validator("email")
    @classmethod
    def normalize_email(cls, value: str) -> str:
        return value.strip().lower()

    @field_validator("display_name")
    @classmethod
    def clean_display_name(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("display_name cannot be empty")
        return value

    @model_validator(mode="after")
    def passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError("password and confirm_password must match")
        return self


class AccountResponse(BaseModel):
    email: str
    display_name: str
