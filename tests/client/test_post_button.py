import pytest
from unittest.mock import patch
from client.ui.window import MainWindow

def test_handle_post(monkeypatch):
    window = MainWindow()
    window.line_edit.setText("Привет")
    window.click_counter = 0

    with patch("client.api.client_api.send_message") as mock_send:
        mock_send.return_value = {"id": 1, "text": "Привет", "click_number": 1}
        window.handle_post()
        mock_send.assert_called_once()
        assert window.line_edit.text() == ""
        assert window.click_counter == 1