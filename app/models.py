from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    first_name: str
    last_name: str
    email: str


class User(UserBase, table=True):
    id: int = Field(primary_key=True)
