from sqlalchemy import asc
from sqlalchemy import delete
from sqlalchemy import desc
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.hotel_booking.models.room import Room
from src.hotel_booking.schemas.room import RoomCreate


async def create_room(session: AsyncSession, room_in: RoomCreate) -> Room:
    room = Room(**room_in.dict())
    session.add(room)
    await session.commit()
    await session.refresh(room)
    return room


async def get_rooms(
    session: AsyncSession, sort_by: str | None = None, ascending: bool = True
):
    query = select(Room)
    if sort_by == "price":
        query = query.order_by(asc(Room.price) if ascending else desc(Room.price))
    elif sort_by == "created_at":
        query = query.order_by(
            asc(Room.created_at) if ascending else desc(Room.created_at)
        )
    result = await session.execute(query)
    return result.scalars().all()


async def delete_room(session: AsyncSession, room_id: int) -> bool:
    result = await session.execute(delete(Room).where(Room.id == room_id))
    await session.commit()
    return result.rowcount > 0


async def get_room_by_id(session: AsyncSession, room_id: int) -> Room | None:
    result = await session.execute(select(Room).where(Room.id == room_id))
    return result.scalars().first()
