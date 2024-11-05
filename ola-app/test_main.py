from fastapi.testclient import TestClient
from fastapi import status
from main import app
import pytest

client = TestClient(app=app)

def get_all_user():
    response = client.get('/users/get-all')
    print(response)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
    "125": {
        "username": "mehrhsad",
        "password": "124312"
    },
    "42": {
        "username": "sarina",
        "password": "1234"
    },
    "1": {
        "username": "mehrshad",
        "password": "07123"
    },
    "1421": {
        "username": "aria5",
        "password": "1232"
    }
}