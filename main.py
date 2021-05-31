import tweepy
import os
import time


consumer_key = (os.getenv("c.key"))
consumer_secret = (os.getenv("c.secret"))

key = (os.getenv("key"))
secret = (os.getenv("secret"))

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)


X = 'tweetid.txt'

def read_tweetid(X):
    file_read = open(X, 'r')
    tweetid = str(file_read.read().strip())
    file_read.close()
    return tweetid

def store_tweetid(y, X):
    file_write = open(X, 'w')
    file_write.write(str(y))
    file_write.close()
    return

def reply():
    print('retrieving tweets...',)
    tweetid = read_tweetid(X)
    tweets = api.mentions_timeline(read_tweetid(X), tweet_mode = 'extended')
    for tweet in reversed(tweets):
        if '#amrevx' in tweet.full_text.lower():
            print("Found a tweet with ID: " + str(tweet.id) + '-' + tweet.full_text + " Replied and Retweeted") 
            y = tweet.id
            api.update_status("@" + tweet.user.screen_name + " Thanks For Using AmrevX" , tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_tweetid(y, X)





while True:
    reply()
    time.sleep(15)




 