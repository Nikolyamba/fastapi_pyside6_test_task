from server.database.session import init_db

init_db()
def test_create_message(client):
    payload = {"text": "Hello", "date": "2025-08-18", "time": "12:00:00", "click_number": 1}
    response = client.post("/message", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "Hello"
    assert data["click_number"] == 1

def test_get_messages_empty_db(client):
    response = client.get("/message?page=1&size=10")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json() == []  # база пустая

def test_create_and_get_message(client):
    payload = {"text": "TestMsg", "date": "2025-08-18", "time": "13:00:00", "click_number": 2}
    client.post("/message", json=payload)

    response = client.get("/message?page=1&size=10")
    data = response.json()
    assert any(msg["text"] == "TestMsg" for msg in data)