from pydantic import BaseSettings
from decouple import config


class Settings(BaseSettings):

    TWITTER_API_KEY: str = config("TWITTER_API_KEY")
    TWITTER_SECRET_KEY: str = config("TWITTER_SECRET_KEY")
    TWITTER_BEARER_TOKEN: str = config("TWITTER_BEARER_TOKEN")
    TWITTER_USERNAME : str = config("TWITTER_USERNAME")

settings = Settings()
