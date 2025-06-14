from fastapi import FastAPI

from src.hotel_booking.api.booking import router as booking_router
from src.hotel_booking.api.room import router as room_router

app = FastAPI()

app.include_router(room_router)
app.include_router(booking_router)
