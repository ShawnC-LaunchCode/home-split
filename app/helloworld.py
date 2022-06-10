import datetime
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello_world():
    return {"message": "Hello world!!!!!!!!!!!!!!!!!&"}


#Keep, takes params, need to create entry
@app.get("/addDebt")
async def addDebt(principal: float = 0, remaining: float = 0, interest_rate: float=4, term_days: int=10950):
    now = datetime.datetime.now()
    term_years=term_days/365
    return {"principal":{principal},"remaining":{remaining},"interest rate": {interest_rate}, "term days":{term_days}, "term years": {term_years}, "created at": {now}, "last updated":{now}}


#Keep, takes params, need to create entry
@app.get("/addUser")
async def addDebt(firstName: str = "first", lastName: str = "lastName"):
    now = datetime.datetime.now()
    fake_id=1
    return {"id":{fake_id},"firstName" : {firstName}, "lastname": {lastName}, "created_at": {now}, "updated_at": {now}}
