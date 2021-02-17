from os import getenv
from pymongo import MongoClient
from bson.objectid import ObjectId


class Database:
    def __init__(self):
        self.client = MongoClient(getenv('MONGO_URI'), w=1)
        self.db = self.client["Cluster0"]
        self.collection = self.db['reviews']
    
    def update(self, id, sentiment):
        query = { "_id": ObjectId(id) }
        props = { "$set": { "sentiment": sentiment, 'reviewed': True } }
        self.collection.update_one(query, props)
