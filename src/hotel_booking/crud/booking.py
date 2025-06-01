from datetime import date

from sqlalchemy import and_
from sqlalchemy import delete
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.hotel_booking.models.booking import Booking
from src.hotel_booking.schemas.booking import BookingCreate


async def create_booking(session: AsyncSession, booking_in: BookingCreate) -> Booking:
    booking = Booking(**booking_in.dict())
    session.add(booking)
    await session.commit()
    await session.refresh(booking)
    return booking


async def get_bookings(session: AsyncSession, hotel_id: int | None = None):
    query = select(Booking)
    if hotel_id is not None:
        query = query.where(Booking.hotel_id == hotel_id)
    result = await session.execute(query)
    return result.scalars().all()


async def delete_booking(session: AsyncSession, booking_id: int) -> bool:
    result = await session.execute(delete(Booking).where(Booking.id == booking_id))
    await session.commit()
    return result.rowcount > 0


async def get_booking_by_id(session: AsyncSession, booking_id: int) -> Booking | None:
    result = await session.execute(select(Booking).where(Booking.id == booking_id))
    return result.scalars().first()


async def check_booking_overlap(
    session: AsyncSession, room_id: int, start_date: date, end_date: date
) -> bool:
    """
    Проверяем, что у заданного номера нет пересечений по датам бронирования.
    Возвращаем True, если есть пересечение, иначе False.
    """
    query = select(Booking).where(
        and_(
            Booking.room_id == room_id,
            Booking.start_date <= end_date,
            Booking.end_date >= start_date,
        )
    )
    result = await session.execute(query)
    return result.scalars().first() is not None
