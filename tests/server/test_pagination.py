from tests.server.test_post import client


def test_pagination():
    for i in range(15):
        client.post("/message", json={
            "text": f"msg {i}",
            "date": "2025-08-17",
            "time": "12:00:00",
            "click_number": i+1
        })

    response = client.get("/message?page=1&size=10")
    data = response.json()
    assert len(data) == 10
    response = client.get("/message?page=2&size=10")
    data = response.json()
    assert len(data) == 5