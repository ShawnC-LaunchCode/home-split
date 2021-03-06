from datetime import datetime
from sqlmodel import SQLModel, Field, func, create_engine
from typing import Optional


class UserBase(SQLModel):
    first_name: str
    last_name: str
    email: str
    created_at: datetime
    updated_at: datetime


class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)


class DebtBase(SQLModel):
    principal: float
    remaining: float
    interest_rate: float
    term_days: int
    created_at: datetime
    updated_at: datetime

class Debt(DebtBase, table=True):
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
