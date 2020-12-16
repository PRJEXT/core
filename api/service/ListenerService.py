import redis
import json

from service.SentAnalysis import SentAnalysis
from service.ReviewService import ReviewService

class ListenerService():
    def __init__(self):
        self.CHANNEL_NAME = "analisys"
        # self.svc = SentAnalysis()
        self.redis = redis.Redis()
        self.reviewService = ReviewService()

        self.pubsub = self.redis.pubsub()
        self.pubsub.psubscribe(self.CHANNEL_NAME)
        self.run()

    def run(self):
        for message in self.pubsub.listen():
            if message["type"]  == 'pmessage':
                data = json.loads(message["data"])
                id = data["id"]
                review = data["review"]
                print(id, review)
                self.reviewService.update(id, review)
                print("Is the right channel", message["data"])

