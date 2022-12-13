from typing import Callable

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine

from afkapi.config import DB_CONNECTION_STRING

db_engine: AsyncEngine = create_async_engine(DB_CONNECTION_STRING, echo=True)
async_sessionmaker: Callable[[], AsyncSession] = sessionmaker(
        db_engine,
        expire_on_commit=True,
        class_=AsyncSession
    )
