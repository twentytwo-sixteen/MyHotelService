from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from src.hotel_booking.db.base import Base
from sqlalchemy.orm import relationship

class Room(Base):
    __tablename__ = "rooms"
    
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    bookings = relationship("Booking", back_populates="room", cascade="all, delete", passive_deletes=True)