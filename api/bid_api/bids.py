from fastapi import APIRouter, Request
from pydantic import BaseModel
from database.bidservice import *
from datetime import datetime
from database import get_db
from typing import Optional

bid_router = APIRouter(prefix="/bid", tags=["API for Bids"])


@bid_router.get('/get_all_bids')
async def get_all_bids():
    all_bids = get_all_bids_db()
    return all_bids

@bid_router.get('/top5_bids_of_item')
async def sort_bids(auction_item_id: int):
    sorted_bids = sort_bids_db(auction_item_id=auction_item_id)
    return sorted_bids



@bid_router.post('/make_bid')
async def make_bid(user_id: int, auction_item_id: int, bid_amount: float):
    new_bid = make_bid_db(user_id=user_id, auction_item_id=auction_item_id, bid_amount=bid_amount)
    return new_bid


@bid_router.put('/greater_bid')
async def greater_bid(user_id: int, auction_item_id: int, plus_bid: float):
    new_bid = greater_bid_db(user_id=user_id, auction_item_id=auction_item_id, plus_bid=plus_bid)
    return new_bid


@bid_router.put('/lower_bid')
async def lower_bid(user_id: int, auction_iem_id: int, minus_bid: float):
    new_bid = lower_bid_db(user_id=user_id, auction_item_id=auction_iem_id, minus_bid=minus_bid)
    return new_bid


@bid_router.delete('/delete_bid')
async def delete_bid(id: int, user_id: int, auction_item_id: int):
    delete = delete_bid_db(id=id, user_id=user_id, auction_item_id=auction_item_id)
    return delete

@bid_router.delete('/delete_user_bids')
async def delete_user_bids(user_id: int):
    delete_bids = delete_user_bids_db(user_id=user_id)
    return delete_bids
