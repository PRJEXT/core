import redis
import json
from os import getenv

from service.SentAnalysis import SentAnalysis
from database.Database import Database


class ListenerService:
    def __init__(self):
        self.CHANNEL_NAME = getenv('REDIS_CHANNEL')
        self.model = SentAnalysis()
        self.redis = redis.Redis()
        self.database = Database()

        self.pubsub = self.redis.pubsub()
        self.pubsub.psubscribe(self.CHANNEL_NAME)
        self.run()

    def run(self):
        for message in self.pubsub.listen():
            if message["type"]  == 'pmessage':
                data = json.loads(message["data"])
                print("Is the right channel", data)
                
                id = data["id"]
                review = data["review"]
                print(f'Id: {id}', f'Review: {review}')
                
                sentiment = self.model.predict(review)
                print(f'Predict: {sentiment}')

                self.database.update(id, sentiment)
                print('Database updated')
