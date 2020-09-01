from fastapi import FastAPI
from db.mongodb import connect_to_mongo,db
import json
from bson.json_util import loads, dumps

app = FastAPI()

app.add_event_handler("startup", connect_to_mongo)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/products")
def read_products():
    return json.loads(dumps(db.client.fastapi.products.find({})))


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}