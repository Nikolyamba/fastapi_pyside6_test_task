from pydantic import BaseModel
from datetime import date, time

class MessageCreate(BaseModel):
    text: str
    date: date
    time: time
    click_number: int

class MessageRead(BaseModel):
    id: int
    text: str
    date: date
    time: time
    click_number: int

    class Config:
        orm_mode = True