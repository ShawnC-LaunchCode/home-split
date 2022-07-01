import os

from sqlmodel import create_engine, SQLModel, Session

DATABASE_URL = "mysql+mysqldb://app:secure_password@127.0.0.1:3306/homesplit_dev"

engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
