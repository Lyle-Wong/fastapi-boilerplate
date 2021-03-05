import logging
from typing import List, cast

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

VERSION = "0.0.1"
API_PREFIX = "/api"
PAGE_PREFIX = "/service"

#
config = Config(".env")

DEBUG: bool = config("DEBUG", cast=bool, default=False)

DATABASE_USER: str = config("DATABASE_USER")
DATABASE_PASSWORD: str = config("DATABASE_PASSWORD")
DATABASE_HOST: str = config("DATABASE_HOST", default="localhost")
DATABASE_PORT: int = config("DATABASE_PORT", cast=int, default=1433)
DATABASE: int = config("DATABASE")

MAX_CONNECTIONS_COUNT: int = config("MAX_CONNECTIONS_COUNT", cast=int, default=10)
MIN_CONNECTIONS_COUNT: int = config("MIN_CONNECTIONS_COUNT", cast=int, default=10)

SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret)

PROJECT_NAME: str = config("PROJECT_NAME", default="")
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS", cast=CommaSeparatedStrings, default="",
)

# logging configuration
LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
LOGURU_LEVEL = "DEBUG" if DEBUG else "INFO"
JSON_LOGS = True if config("JSON_LOGS", default="0") == "1" else False

