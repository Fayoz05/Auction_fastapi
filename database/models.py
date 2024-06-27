from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    phone_number = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    reg_date = Column(DateTime)


class AuctionItem(Base):
    __tablename__ = 'auction_items'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    starting_bid = Column(Float, nullable=False)
    auction_created = Column(DateTime)
    auction_end_time = Column(DateTime)
    user_fk = relationship(User, foreign_keys=[user_id], lazy='subquery')


class AuctionPhoto(Base):
    __tablename__ = 'auction_photo'
    id = Column(Integer, autoincrement=True, primary_key=True)
    auction_item_id = Column(Integer, ForeignKey('auction_items.id'))
    photo_path = Column(String, nullable=False)
    reg_date = Column(DateTime)

    auction_item_fk = relationship(AuctionItem, foreign_keys=[auction_item_id], lazy='subquery')


class Bid(Base):
    __tablename__ = 'bids'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    auction_item_id = Column(Integer, ForeignKey('auction_items.id'))
    bid_amount = Column(Float, nullable=False)

    user_fk = relationship(User, foreign_keys=[user_id], lazy='subquery')
    auction_item_fk = relationship(AuctionItem, foreign_keys=[auction_item_id], lazy='subquery')
