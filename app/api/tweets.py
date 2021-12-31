from fastapi import APIRouter
from app.config import settings

route = APIRouter(
    tags=["app"],
    responses={
        404: {"status_code": 404, "msg": "invalid_url"}
    }
)

@route.get("/send-tweets")
async def send_tweets():
    return {'msg':'{}'.format(settings.TWITTER_API_KEY)}


def get_tweets():
    pass