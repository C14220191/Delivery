import datetime
from sqlalchemy import (
    DECIMAL, Column, DateTime, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base

class Base(object):
    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        nullable=False
    )

DeclarativeBase = declarative_base(cls=Base)

class Delivery(DeclarativeBase):
    __tablename__ = "deliveries"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tujuan = Column(String, nullable=False)
    jarak = Column(Integer, nullable=False)
    notes = Column(String)
    harga_delivery = Column(DECIMAL(18, 2), nullable=False)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    member_id = Column(Integer, ForeignKey('members.id'), nullable=False) 
