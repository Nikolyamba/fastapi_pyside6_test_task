from client.ui.MsgListModel import MessageListModel


def test_update_data():
    model = MessageListModel()
    data = [{"id":1,"text":"hi","date":"2025-08-17","time":"12:00:00","click_number":1}]
    model.update_data(data)
    assert model.rowCount() == 1
    assert "hi" in model.data(model.index(0))