from pymongo import MongoClient
from pymongo.collection import Collection


class DataBase:
    client: MongoClient = None

    def get_collection(self, collection):
        if self.client is not None:
            return self.client.get_database("fastapi").get_collection(collection)
        else:
            return self.client

db = DataBase()


def get_database() -> MongoClient:
    return db.client


def get_collection(collection: str) -> Collection:
    return db.get_collection(collection)


def connect_to_mongo():
    db.client = MongoClient('mongodb://localhost:27017/')
