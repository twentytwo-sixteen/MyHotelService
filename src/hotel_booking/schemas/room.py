from datetime import datetime

from pydantic import BaseModel
from pydantic import Field


class RoomCreate(BaseModel):
    description: str = Field(..., example="Deluxe Room")
    price: int = Field(..., example=120)


class RoomOut(RoomCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
