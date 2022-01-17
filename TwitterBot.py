import tweepy
import time
api_key = 'kle9H0SMRSBgTfc0y98uqTUqP'
api_key_secret ="S5RNvfdKuJqnFHIfv35QEreFXgR4oBYbUNJ6vn81wbqiEC5L5u"
access_token = "1435556372779782146-ycNt1HJAbGJRCZQ5lmbqHVU8lFXHga"
access_token_secret = "hPYGzNHxyRfWNQmW8cMKXreEB6TpnlqWJWiBqsnzEPxDW"

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

keyword = 'python'
#Tweets containing the keyword above will be returned from the twitter timeline

no_tweets = 5
#The number of tweets containing the keyword that we want to obtain

for tweet in tweepy.Cursor(api.search, keyword).items(no_tweets):
    try:
        print('Liked Tweet')
        tweet.retweet()
        time.sleep(10)     # Program will wait 10 seconds before liking another tweet
    except tweepy.TweepError as error:
        print(error.reason)
    except StopIteration:
        break







