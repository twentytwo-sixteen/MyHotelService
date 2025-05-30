from sqlalchemy import Column, Integer, Date, ForeignKey
from src.hotel_booking.db.base import Base
from sqlalchemy.orm import relationship


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id", ondelete="CASCADE"), nullable=False)
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)

    room = relationship("Room", back_populates="bookings")
