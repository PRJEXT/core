from pymongo import MongoClient

url = 'mongodb+srv://ian_guimaraes:NVaTKD4ASJtZIszG@cluster0.pfbqd.mongodb.net/Cluster0?retryWrites=true&w=majority'

class Database():
    def __init__(self):
        self.client = MongoClient(url)
        self.db = self.client["Cluster0"]

