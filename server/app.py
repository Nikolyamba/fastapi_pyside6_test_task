import uvicorn
from fastapi import FastAPI

from server.database.session import init_db
from server.routes.message import msg_router

app = FastAPI()

@app.on_event("startup")
def start_db():
    init_db()

app.include_router(msg_router)


if __name__ == "__main__":
    uvicorn.run("server.app:app", host="127.0.0.1", port=8004)