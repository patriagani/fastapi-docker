from fastapi import FastAPI
from .db.mongodb import close_mongo_connection, connect_to_mongo

app = FastAPI()

app.add_event_handler("startup", connect_to_mongo)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}