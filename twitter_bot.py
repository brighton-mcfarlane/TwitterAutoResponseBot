import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import StreamListener
from random import choice
import random
from os import environ

consumer_key = environ["consumer_key"]
consumer_secret = environ["consumer_secret"]
access_token = environ["access_token"]
access_secret = environ["access_secret"]

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)



api = tweepy.API(auth)

api.create_friendship(#twitter user id)

responses = ["Thank you for replying!", "I hope your day is going great!", "Keep up the great work!", "What an interesting perspective!", "Love your style!"]

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if status.user.id_str != #'twitter user id':
            return
        #response = random.choice(responses(0, -1)(i) for i in responses)
        api.update_status(f"{random.choice(responses)}", status.id)



myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(follow=[#'twitter user Id'], is_async=True)





