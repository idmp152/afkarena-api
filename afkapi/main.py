import asyncio
from typing import Iterable

import uvicorn #type: ignore

from fastapi import FastAPI, APIRouter
from sqlalchemy.ext.asyncio import AsyncEngine

from afkapi.api.heroes import heroes_router
from afkapi.core.models import Base
from afkapi.core import db_engine
from afkapi.config import HOST, PORT

app: FastAPI = FastAPI()
routers: Iterable[APIRouter] = (heroes_router,)


# TODO: Swagger OpenAPI description and tags metadata

async def start_db_engine_async(engine: AsyncEngine, schema) -> None:
    """Asynchronously starts the database engine"""
    async with engine.begin() as conn:
        await conn.run_sync(schema.metadata.create_all)

def main() -> None:
    """Main function"""
    for router in routers:
        app.include_router(router)
    asyncio.run(start_db_engine_async(db_engine, Base))
    uvicorn.run(app,
                host=HOST,
                port=PORT
                )

if __name__ == "__main__":
    main()
