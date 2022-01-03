from typing import Dict
from fastapi import APIRouter
from app.config import settings

from app.utils.helpers import send_email, get_tweets

route = APIRouter(
    tags=["app"],
    responses={
        404: {"status_code": 404, "msg": "invalid_url"}
    }
)


@route.get("/send-tweets")
async def send_tweets():
    tweet, tweet_id = get_tweets()
    if all([tweet, tweet_id]):
       send_email(tweet=tweet, tweet_id=tweet_id)
       return {'msg': 'Success'}
    return {'msg': 'No Cryto Tweet'}
