import requests
from datetime import datetime

API_URL = "http://127.0.0.1:8004"

def send_message(text: str, click_number: int) -> dict:
    now = datetime.now()

    payload = {
        "text": text,
        "date": now.date().isoformat(),
        "time": now.time().strftime("%H:%M:%S"),
        "click_number": click_number
    }

    r = requests.post(f"{API_URL}/message", json=payload)
    r.raise_for_status()
    return r.json()

def get_messages(page: int = 1, size: int = 20) -> list[dict]:
    r = requests.get(f"{API_URL}/message?page={page}&size={size}")
    r.raise_for_status()
    return r.json()