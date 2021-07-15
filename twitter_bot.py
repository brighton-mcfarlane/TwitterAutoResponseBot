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

responses = ["Silence, you Canadian oppressor", "How about you shut up about issues you know nothing about.", "Woooowww...coming from a white colonizer", "Your ethnicity is a sham", "Go back to Britain...Oh wait..."]

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if status.user.id_str != '1407713509950083074':
            return
        bobified_string = self.bobify(status.text)
        #response = random.choice(responses(0, -1)(i) for i in responses)
        api.update_status(f"@PastaAndCannoli {bobified_string[0:35]}...{random.choice(responses)}", status.id)


    def bobify(self, message):
        bobify_string =''.join(choice((str.upper, str.lower))(c) for c in message)

        return bobify_string


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(follow=['1407713509950083074'], is_async=True)

# username = "PastaAndCannoli"

# user = api.get_user(username)

# id = user.id_str

# print(id)

#1407713509950083074



