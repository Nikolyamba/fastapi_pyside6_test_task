from typing import List

from fastapi import APIRouter, Depends, Query

from sqlalchemy.orm import Session

from server.database.get_db import get_db
from server.models.message_model import Message
from server.models.pydantics import MessageRead, MessageCreate

msg_router = APIRouter()

@msg_router.post("/message", response_model=MessageRead)
async def create_msg(data: MessageCreate, db: Session = Depends(get_db)) -> dict:
    new_message = Message(text = data.text,
                          date = data.date,
                          time = data.time,
                          click_number = data.click_number)
    db.add(new_message)
    db.commit()
    db.refresh(new_message)

    return new_message

@msg_router.get("/message", response_model=List[MessageRead])
async def get_msg(db: Session = Depends(get_db), page: int = Query(1, gt=0), size: int = Query(10, ge=1, le=50)):
    offset = (page - 1) * size
    messages = db.query(Message).offset(offset).limit(size).all()
    return messages
