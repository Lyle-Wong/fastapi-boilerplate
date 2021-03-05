from typing import Callable
from loguru import logger

from src.core.db import engine

def create_start_app_handler() -> Callable:  # type: ignore
    async def startup():
        engine.connect().close()
    return startup


def create_stop_app_handler() -> Callable:  # type: ignore
    @logger.catch
    async def shutdown():
        pass

    return shutdown
