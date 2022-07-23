from urllib import response
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.helloworld import app

client = TestClient(app)

def test_hello_world():
    response = client.get("/")
    assert response.status_code ==200
    
def test_create_user():
    body = {
        "first_name": "Test1",
        "last_name": "LastName",
        "email":"test@testing.test"
    }
    response = client.post("/users", json=body)
    assert response.status_code == 200
    assert response.json()["id"]

