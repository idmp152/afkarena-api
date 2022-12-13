from sqlalchemy.future import select
from fastapi import APIRouter, HTTPException, status

from afkapi.core import async_sessionmaker
from afkapi.core.models import heroes as model_heroes
from afkapi.core.schemas import heroes as schema_heroes

heroes_router: APIRouter = APIRouter(prefix="/api/heroes")

HERO_SLUG_DOES_NOT_EXIST_ERROR: HTTPException = HTTPException(
                                    detail="Hero with the given slug does not exist.",
                                    status_code=status.HTTP_400_BAD_REQUEST)

# TODO: Add Swagger tags

@heroes_router.get("/{hero_slug}", response_model=schema_heroes.Hero)
async def get_hero_by_slug(hero_slug: str):
    """Gets the AFK Arena hero by its name."""
    # TODO: Add Redis caching
    async with async_sessionmaker() as sess:
        async with sess.begin():
            hero_row = (await sess.execute(select(model_heroes.Hero
                        ).where(model_heroes.Hero.slug == hero_slug))).fetchone()
            hero = hero_row[0] if hero_row else None
            if not hero:
                raise HERO_SLUG_DOES_NOT_EXIST_ERROR
            hero_model = schema_heroes.Hero.from_orm(hero)

    return hero_model
