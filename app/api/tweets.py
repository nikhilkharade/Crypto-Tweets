from typing import Dict
from fastapi import APIRouter
from app.config import settings

from app.utils.helpers import is_keyword_in_tweet,get_tweets

route = APIRouter(
    tags=["app"],
    responses={
        404: {"status_code": 404, "msg": "invalid_url"}
    }
)


@route.get("/send-tweets")
async def send_tweets():
    tweet,tweet_id = get_tweets()
    if all([tweet,tweet_id]):
        #function of sending mail
        pass
    return {'msg': 'Success'}


