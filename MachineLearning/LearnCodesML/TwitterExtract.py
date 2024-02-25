import tweepy
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

# # Define your search query
path="../../Data/twitterAPI/"
twitterAuth=pd.read_csv(os.path.join(path,"twitterAPI.csv"))
consumer_key=twitterAuth['API Key'][0]
consumer_secret=twitterAuth['API Secret'][0]
access_token=twitterAuth['Access Token'][0]
access_token_secret=twitterAuth['Access Token Secret'][0]
search_query = "depression -filter:retweets"

print(twitterAuth)

# # Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# # Define your search query
search_query = "depression -filter:retweets"

# # Collect tweets
tweets = tweepy.Cursor(api.search_tweets, q=search_query, lang="en", tweet_mode='extended').items(100)

# Process and print tweets
for tweet in tweets:
    print(tweet.full_text)
