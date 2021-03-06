from pydantic import BaseSettings
from decouple import config


class Settings(BaseSettings):

    TWITTER_API_KEY: str = config("TWITTER_API_KEY")
    TWITTER_SECRET_KEY: str = config("TWITTER_SECRET_KEY")
    TWITTER_BEARER_TOKEN: str = config("TWITTER_BEARER_TOKEN")
    TWITTER_USERNAME : str = config("TWITTER_USERNAME")
    TWITTER_ACCESS_TOKEN : str = config("TWITTER_ACCESS_TOKEN")
    TWITTER_ACCESS_TOKEN_SECRET : str = config("TWITTER_ACCESS_TOKEN_SECRET")
    EMAIL_ID : str = config("EMAIL_ID")
    EMAIL_PASSWORD : str = config("EMAIL_PASSWORD")
    CLIENT_MAIL_ID : str = config("CLIENT_MAIL_ID")
settings = Settings()
