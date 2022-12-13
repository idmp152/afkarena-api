import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean

from afkapi.core.models import Base


# TODO: Add skills and image fields

class Hero(Base): #type: ignore
    """AFK Arena hero model."""
    __tablename__ = "hero_hero"

    id: Column = Column(Integer, primary_key=True)
    name: Column = Column(String(50))
    faction: Column = Column(String(50))
    description: Column = Column(String(255), nullable=True)
    h_class: Column = Column(String(50), nullable=True)
    role: Column = Column(String(50), nullable=True)
    position: Column = Column(String(50), nullable=True)
    artifact: Column = Column(String(50), nullable=True)
    union: Column = Column(String(50), nullable=True)
    h_type: Column = Column(String(50), nullable=True)
    status: Column = Column(String(255), nullable=True)
    lore: Column = Column(String, nullable=True)

    slug: Column = Column(
        String(155),
        unique=True,
        index=True,
        nullable=True
    )

    time_added_to_site: Column = Column(DateTime, default=datetime.datetime.now)
    time_update: Column = Column(DateTime, default=datetime.datetime.now,
                                                onupdate=datetime.datetime.now)
    is_published: Column = Column(Boolean, default=True)
