from pymongo import MongoClient

url = ''

class Database():
    def __init__(self):
        self.client = MongoClient(url)
        self.db = self.client["Cluster0"]

