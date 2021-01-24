from os import getenv
from pymongo import MongoClient


class Database:
    def __init__(self):
        self.client = MongoClient(getenv('MONGO_URI'))
        self.db = self.client["Cluster0"]
