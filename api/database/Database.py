from os import getenv
from pymongo import MongoClient
from bson.objectid import ObjectId


class Database:
    def __init__(self):
        self.client = MongoClient(getenv('MONGO_URI'))
        self.COLLECTION = 'reviews'
        self.db = self.client["Cluster0"]
        self.collection = self.db[self.COLLECTION]
    
    def update(self, id, sentiment):
        query = { "_id": ObjectId(id) }
        props = { "$set": { "sentiment": sentiment, 'reviewed': True } }
        updated = self.collection.update_one(query, props)
        print(updated)
