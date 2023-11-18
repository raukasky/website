from enum import Enum

from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(find_dotenv())


class Settings(BaseSettings):
    class Environment(str, Enum):
        local = 'local'
        dev = 'dev'
        prod = 'prod'

    # Essential config
    PROJECT_NAME: str
    ENVIRONMENT: Environment


settings = Settings()
