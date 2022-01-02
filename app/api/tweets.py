from fastapi import APIRouter
from app.config import settings
import tweepy as tw

route = APIRouter(
    tags=["app"],
    responses={
        404: {"status_code": 404, "msg": "invalid_url"}
    }
)


@route.get("/send-tweets")
async def send_tweets():
    get_tweets()
    return {'msg': '{}'.format(settings.TWITTER_API_KEY)}


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
    keywords = get_crypto_keywords()
    for i in tweets:
        tweet_text = i.full_text
        if tweet_text in []:
            tweet_id = i.id
            #send mail function 

