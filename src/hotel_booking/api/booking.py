from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.hotel_booking.schemas.booking import BookingCreate, BookingOut
from src.hotel_booking.db.session import get_session
from src.hotel_booking.crud.booking import (
    create_booking,
    get_bookings,
    delete_booking,
    get_booking_by_id,
    check_booking_overlap,
)

router = APIRouter(prefix="/bookings", tags=["bookings"])

@router.post("/", response_model=BookingOut)
async def create_booking_view(booking_in: BookingCreate, session: AsyncSession = Depends(get_session)):
    overlap = await check_booking_overlap(
        session,
        room_id=booking_in.room_id,
        start_date=booking_in.start_date,
        end_date=booking_in.end_date,
    )
    if overlap:
        raise HTTPException(status_code=400, detail="This room is already booked for the selected dates.")
    
    return await create_booking(session, booking_in)

@router.get("/", response_model=list[BookingOut])
async def list_bookings(hotel_id: int | None = None, session: AsyncSession = Depends(get_session)):
    return await get_bookings(session, hotel_id)

@router.get("/{booking_id}", response_model=BookingOut)
async def get_booking_view(booking_id: int, session: AsyncSession = Depends(get_session)):
    booking = await get_booking_by_id(session, booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@router.delete("/{booking_id}", status_code=204)
async def delete_booking_view(booking_id: int, session: AsyncSession = Depends(get_session)):
    deleted = await delete_booking(session, booking_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Booking not found")
