# from pydantic_settings import BaseSettings

# class Settings(BaseSettings):
#     APP_NAME: str = "Sentiment Analyzer"
#     DEBUG: bool = True

#     class Config:
#         env_file = ".env"

# settings = Settings()
# ----------------------------------------------------------------------------

from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    APP_NAME: str = "Sentiment Analyzer"
    DEBUG: bool = True

    model_config = {
        "env_file": ".env"
    }

settings = Settings()

