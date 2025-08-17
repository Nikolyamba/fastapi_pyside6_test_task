from client.ui.MsgListModel import MessageListModel
from PySide6.QtWidgets import (
    QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QListView
)

from client.api.api_client import send_message, get_messages

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 800, 500)
        self.setWindowTitle("Тестовое задание")

        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Введите сообщение...")

        self.post_button = QPushButton("Post")
        self.get_button = QPushButton("Get")
        self.list_view = QListView()

        self.model = MessageListModel()
        self.list_view.setModel(self.model)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.post_button)
        button_layout.addWidget(self.get_button)

        layout.addWidget(self.line_edit)
        layout.addLayout(button_layout)
        layout.addWidget(self.list_view)

        central_widget.setLayout(layout)

        self.click_counter = 0

        self.post_button.clicked.connect(self.handle_post)
        self.get_button.clicked.connect(self.handle_get)

    def handle_post(self):
        text = self.line_edit.text().strip()
        if not text:
            return

        self.click_counter += 1
        try:
            send_message(text, self.click_counter)
            self.line_edit.clear()
            self.handle_get()
        except Exception as e:
            print("Ошибка при отправке:", e)

    def handle_get(self):
        try:
            messages = get_messages()
            self.model.update_data(messages)
        except Exception as e:
            print("Ошибка при получении:", e)
