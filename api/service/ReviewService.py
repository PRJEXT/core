from database.Database import Database
from bson.objectid import ObjectId

class ReviewService():
    def __init__(self):
        self.COLLECTION = 'reviews'
        self.db = Database().db
        self.collection = self.db['reviews']

    def update(self, id, sentiment):
        query = { "_id": ObjectId(id) }
        props = { "$set": { "sentiment": sentiment, 'reviewed': True } }
        updated = self.collection.update_one(query, props)
        print(updated)
