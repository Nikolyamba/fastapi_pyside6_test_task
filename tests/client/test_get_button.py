from unittest.mock import patch

from client.ui.window import MainWindow


def test_handle_get(monkeypatch):
    window = MainWindow()
    dummy_data = [{"id":1,"text":"msg","date":"2025-08-17","time":"12:00:00","click_number":1}]
    with patch("client.api.client_api.get_messages", return_value=dummy_data):
        window.handle_get()
        assert window.model.rowCount() == 1