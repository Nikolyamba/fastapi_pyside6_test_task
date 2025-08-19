import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from server.app import app
from server.database.session import Base
from server.database.get_db import get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function", autouse=True)
def setup_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="function")
def client():
    return TestClient(app)

def test_create_message(client):
    data = {
        "text": "Hello world!",
        "date": "2025-08-19",
        "time": "12:00:00",
        "click_number": 1
    }
    response = client.post("/message", json=data)
    assert response.status_code == 200
    result = response.json()
    assert result["text"] == "Hello world!"
    assert result["click_number"] == 1
    assert "id" in result

def test_get_messages(client):
    client.post("/message", json={
        "text": "Test msg",
        "date": "2025-08-19",
        "time": "12:30:00",
        "click_number": 2
    })
    response = client.get("/message")
    assert response.status_code == 200
    result = response.json()
    assert isinstance(result, list)
    assert len(result) == 1  # теперь будет ровно 1 запись
    assert result[0]["text"] == "Test msg"

def test_pagination(client):
    client.post("/message", json={
        "text": "msg1",
        "date": "2025-08-19",
        "time": "13:00:00",
        "click_number": 1
    })
    client.post("/message", json={
        "text": "msg2",
        "date": "2025-08-19",
        "time": "13:30:00",
        "click_number": 2
    })

    response1 = client.get("/message?page=1&size=1")
    assert response1.status_code == 200
    result1 = response1.json()
    assert len(result1) == 1
    assert result1[0]["text"] == "msg1"

    response2 = client.get("/message?page=2&size=1")
    assert response2.status_code == 200
