import os

from sqlmodel import create_engine, SQLModel, Session

DATABASE_URL = "127.0.0.1:3306"

engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
