from tests.server.test_post import client


def test_get_messages():
    response = client.get("/message?page=1&size=10")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)