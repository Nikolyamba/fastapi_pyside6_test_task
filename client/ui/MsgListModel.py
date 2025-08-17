from PySide6.QtCore import QStringListModel

class MessageListModel(QStringListModel):

    def update_data(self, messages: list[dict]):
        data = [
            f"{m['id']}: {m['text']} ({m['date']} {m['time']}, click={m['click_number']})"
            for m in messages
        ]
        self.setStringList(data)