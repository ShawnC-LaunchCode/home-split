import datetime
from email.policy import default
from typing import Optional
from fastapi import FastAPI
from .models import Debt, User
from sqlmodel import Field, Session, SQLModel, create_engine

app = FastAPI()


engine = create_engine(
    "mysql+mysqldb://app:secure_password@localhost:3360/homesplit_dev", echo=True
)


@app.get("/")
async def hello_world():
    return {"message": "Hello world!!!!!!!!!!!!!!!!!&"}


@app.post("/users")
def create_user(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

@app.get("/users/{user_id}")
def get_user(user_id: int):
    with Session(engine) as session:
        user=session.get(User, user_id)
    return user



@app.post("/users/{user_id}/debts/{debt_id}")
def create_debt(debt:Debt):
    with Session(engine) as session:
        session.add(debt)
        #session.commit()
        #session.refresh(debt)
        return debt
