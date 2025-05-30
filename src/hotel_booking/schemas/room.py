from pydantic import BaseModel, Field
from datetime import datetime

class RoomCreate(BaseModel):
    description: str = Field(..., example="Deluxe Room")
    price: int = Field(..., example=120)

class RoomOut(RoomCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True