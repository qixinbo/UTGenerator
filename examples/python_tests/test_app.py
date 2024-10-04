import pytest
from fastapi.testclient import TestClient
from app import app
from datetime import date

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI application!"}
import pytest
from fastapi.testclient import TestClient
from app import app
from datetime import date

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI application!"}

def test_current_date():
    response = client.get("/current-date")
    assert response.status_code == 200
    assert 'date' in response.json()
    assert datetime.fromisoformat(response.json()['date'])

def test_add_positive_numbers():
    response = client.get("/add/3/4")
    assert response.status_code == 200
    assert response.json() == {"result": 7}

def test_add_negative_numbers():
    response = client.get("/add/-1/-1")
    assert response.status_code == 200
    assert response.json() == {"result": -2}

def test_subtract_positive_numbers():
    response = client.get("/subtract/5/3")
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_subtract_negative_numbers():
    response = client.get("/subtract/-1/-1")
    assert response.status_code == 200
    assert response.json() == {"result": 0}

def test_multiply_positive_numbers():
    response = client.get("/multiply/3/4")
    assert response.status_code == 200
    assert response.json() == {"result": 12}

def test_multiply_negative_numbers():
    response = client.get("/multiply/-3/-4")
    assert response.status_code == 200
    assert response.json() == {"result": 12}

def test_divide_positive_numbers():
    response = client.get("/divide/6/3")
    assert response.status_code == 200
    assert response.json() == {"result": 2.0}

def test_divide_by_zero():
    response = client.get("/divide/6/0")
    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot divide by zero"}

def test_square_positive_number():
    response = client.get("/square/5")
    assert response.status_code == 200
    assert response.json() == {"result": 25}

def test_square_negative_number():
    response = client.get("/square/-5")
    assert response.status_code == 200
    assert response.json() == {"result": 25}

def test_sqrt_positive_number():
    response = client.get("/sqrt/9")
    assert response.status_code == 200
    assert response.json() == {"result": 3.0}

def test_sqrt_negative_number():
    response = client.get("/sqrt/-1")
    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot take square root of a negative number"}

def test_is_palindrome_true():
    response = client.get("/is-palindrome/racecar")
    assert response.status_code == 200
    assert response.json() == {"is_palindrome": True}

def test_is_palindrome_false():
    response = client.get("/is-palindrome/hello")
    assert response.status_code == 200
    assert response.json() == {"is_palindrome": False}

def test_days_until_new_year():
    response = client.get("/days-until-new-year")
    assert response.status_code == 200
    assert 'days_until_new_year' in response.json()
    assert isinstance(response.json()['days_until_new_year'], int)

def test_echo():
    response = client.get("/echo/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "hello"}