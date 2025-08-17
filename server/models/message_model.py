from datetime import datetime

from sqlalchemy import Column, Integer, String, Date, Time

from server.database.session import Base

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    text = Column(String(150), unique=False, nullable=False)
    date = Column(Date, nullable=False, default=datetime.utcnow().date)
    time = Column(Time, nullable=False, default=datetime.utcnow().time)
    click_number = Column(Integer, nullable=False)