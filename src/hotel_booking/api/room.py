from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.hotel_booking.crud.room import create_room
from src.hotel_booking.crud.room import delete_room
from src.hotel_booking.crud.room import get_room_by_id
from src.hotel_booking.crud.room import get_rooms
from src.hotel_booking.db.session import get_session
from src.hotel_booking.schemas.room import RoomCreate
from src.hotel_booking.schemas.room import RoomOut

router = APIRouter(prefix="/rooms", tags=["rooms"])


@router.post("/", response_model=RoomOut)
async def create_room_view(
    room_in: RoomCreate, session: AsyncSession = Depends(get_session)
):
    return await create_room(session, room_in)


@router.get("/", response_model=list[RoomOut])
async def list_rooms(
    sort_by: str = Query(None, enum=["price", "created_at"]),
    ascending: bool = Query(True),
    session: AsyncSession = Depends(get_session),
):
    return await get_rooms(session, sort_by, ascending)


@router.delete("/{room_id}", status_code=204)
async def delete_room_view(room_id: int, session: AsyncSession = Depends(get_session)):
    deleted = await delete_room(session, room_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Room not found")


@router.get("/{room_id}", response_model=RoomOut)
async def get_room_view(room_id: int, session: AsyncSession = Depends(get_session)):
    room = await get_room_by_id(session, room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room
