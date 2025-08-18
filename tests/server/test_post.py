import pytest
from fastapi.testclient import TestClient
from server.app import app

client = TestClient(app)

def test_post_message():
    payload = {
        "text": "Тестовое сообщение",
        "date": "2025-08-17",
        "time": "12:34:56",
        "click_number": 1
    }
    response = client.post("/message", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == payload["text"]
    assert data["click_number"] == payload["click_number"]