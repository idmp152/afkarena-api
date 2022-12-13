from pydantic import BaseModel

# TODO: Add skills and image fields

class Hero(BaseModel):
    """AFK Arena hero response schema."""
    name: str
    faction: str
    description: str
    h_class: str
    role: str
    position: str
    artifact: str
    union: str
    h_type: str
    status: str
    lore: str

    class Config:
        """Pydantic config."""
        orm_mode = True
