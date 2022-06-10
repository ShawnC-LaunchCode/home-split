from sqlmodel import SQLModel, Field


class User(SQLModel):
    id: int = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
