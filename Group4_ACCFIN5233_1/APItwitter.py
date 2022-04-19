import tweepy
import configparser
import pandas as pd

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# search tweets
keywords = '@doodles'
# keywords =
limit=500000

tweets = tweepy.Cursor(api.search_tweets, q=keywords, count=200, tweet_mode='extended').items(limit)
# tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')

#help(tweepy.Cursor)

# create DataFrame ,
columns = ['Time','User', 'Tweet']
data = []

for tweet in tweets:
    data.append([tweet.created_at,tweet.user.screen_name, tweet.full_text])
#
print(data)

df = pd.DataFrame(data, columns=columns)

print(df)

df.to_csv('doodles500kfinal.csv')

