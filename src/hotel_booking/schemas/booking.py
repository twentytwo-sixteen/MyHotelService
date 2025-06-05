from datetime import date

from pydantic import BaseModel
from pydantic import Field


class BookingCreate(BaseModel):
    room_id: int = Field(..., example=1)
    start_date: date = Field(..., example="2025-06-01")
    end_date: date = Field(..., example="2025-06-05")


class BookingOut(BookingCreate):
    id: int

    class Config:
        orm_mode = True
