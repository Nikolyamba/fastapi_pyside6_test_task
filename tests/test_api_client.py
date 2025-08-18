import pytest
import requests
from client.api import api_client

def test_send_message_success(requests_mock):
    url = f"{api_client.API_URL}/message"
    fake_response = {"id": 1, "text": "Hello", "date": "2025-08-18", "time": "12:00:00", "click_number": 1}
    requests_mock.post(url, json=fake_response, status_code=200)

    result = api_client.send_message("Hello", 1)
    assert result["text"] == "Hello"
    assert result["click_number"] == 1


def test_get_messages_success(requests_mock):
    url = f"{api_client.API_URL}/message?page=1&size=20"
    fake_response = [{"id": 1, "text": "Hi", "date": "2025-08-18", "time": "12:00:00", "click_number": 1}]
    requests_mock.get(url, json=fake_response, status_code=200)

    result = api_client.get_messages()
    assert isinstance(result, list)
    assert result[0]["text"] == "Hi"


def test_send_message_error(requests_mock):
    url = f"{api_client.API_URL}/message"
    requests_mock.post(url, status_code=500)

    with pytest.raises(requests.exceptions.HTTPError):
        api_client.send_message("Bad", 99)