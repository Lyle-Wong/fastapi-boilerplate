
from typing import Iterator
from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session
from src.config import DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE
from fastapi_utils.session import FastAPISessionMaker
from functools import lru_cache

# SQLALCHEMY_DATABASE_URL = "mysql://root:Root1024@localhost/fastapi"
# engine = create_engine(DATABASE_URL.__str__())
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base: DeclarativeMeta = declarative_base()

# async db query
# database = databases.Database(DATABASE_URL)

SQLALCHEMY_DATABASE_URI = f"mssql+pymssql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE}?charset=utf8"

engine = create_engine(
    f"mssql+pymssql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE}?charset=utf8",
    pool_size=10
    )


@lru_cache()
def _get_fastapi_sessionmaker() -> FastAPISessionMaker:
    return FastAPISessionMaker(SQLALCHEMY_DATABASE_URI)

def get_db() -> Iterator[Session]:
    yield from _get_fastapi_sessionmaker().get_db()