from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))

class Provider(Base):

    __tablename__ = 'providers'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))

class Bus(Base):

    __tablename__ = 'buses'
    id = Column(Integer, primary_key=True , nullable=False)
    provider_id = Column(Integer, ForeignKey("providers.id", ondelete="CASCADE"), nullable=False)
    model = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    is_available = Column(Boolean, server_default="TRUE", nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))

class Ride(Base):

    __tablename__ = "rides"

    id = Column(Integer, primary_key=True, nullable=False)
    provider_id = Column(Integer, ForeignKey("providers.id", ondelete="CASCADE"),nullable=False)
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    depature_time = Column(TIMESTAMP(timezone=True), nullable=False)
    arrival_time = Column(TIMESTAMP(timezone=True), nullable=False)
    

class Booking(Base):

    __tablename__ = "bookings"

    id = Column(Integer, primary_key =True, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    ride_id = Column(Integer, ForeignKey("rides.id", ondelete="CASCADE") , nullable=False)
    reserved_seats = Column(Integer, nullable=False)

class Review(Base):

    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, nullable=False)
    provider_id = Column(Integer,ForeignKey("providers.id", ondelete="CASCADE"), nullable=False)
    ratings = Column(Integer, nullable=False)
    comments = Column(String, nullable=False)


