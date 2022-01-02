from typing import List
import pandas as pd
from typing import List,Dict
from app.config import settings
import tweepy as tw
import os

def get_crypto_keywords() -> List:
    current_directory = os.getcwd()
    keywords_df = pd.read_csv('{}/app/utils/crypto_keywords.csv'.format(current_directory))
    keywords_df['buzzwords'].to_list()
    if not keywords_df.empty:
        data = keywords_df['buzzwords'].to_list()
        final_data = [x.lower() for x in data]
        return final_data
    return []


def is_keyword_in_tweet(tweet : Dict) -> bool:
    keywords = get_crypto_keywords()
    for keyword in keywords:
        if keyword in tweet.lower():
            return True
    return False


def get_tweets():

    person_to_track = settings.TWITTER_USERNAME
    auth = tw.OAuthHandler(settings.TWITTER_API_KEY,
                           settings.TWITTER_SECRET_KEY)
    auth.set_access_token(settings.TWITTER_ACCESS_TOKEN,
                          settings.TWITTER_ACCESS_TOKEN_SECRET)
    api = tw.API(auth, wait_on_rate_limit=True)
    tweets = api.user_timeline(screen_name=person_to_track,
                               count=30,
                               include_rts=False,
                               tweet_mode='extended'
                               )
    
    for tweet in tweets:
        is_crypto_tweet = is_keyword_in_tweet(tweet.full_text)
        print(is_crypto_tweet)
        if is_crypto_tweet:
            tweet_text = tweet.full_text
            tweet_id = tweet.id
            return tweet_text,tweet_id
    
    return '',''