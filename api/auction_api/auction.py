from fastapi import APIRouter, Request
from pydantic import BaseModel
from database.auctionservice import *
from datetime import datetime
from database import get_db
from typing import Optional

auction_router = APIRouter(prefix="/auction", tags=["API for Auction"])


@auction_router.get('/all_auctions')
async def get_all_auctions():
    data = all_auctions_db()
    return data


@auction_router.get('/get_exact_item')
async def get_exact_item(id: int):
    exact_item = get_exact_item_db(id=id)
    return exact_item


@auction_router.post('/create_auction')
async def create_auction(user_id: int, name: str, description: str, starting_bid: float, duration: int):
    auction = create_auction_db(user_id=user_id, name=name, description=description, starting_bid=starting_bid,
                                duration=duration)
    return auction


@auction_router.put('/change_name')
async def change_auction_name(id: int, new_name: str):
    auction_name = change_auction_name_db(id=id, new_name=new_name)
    return auction_name


@auction_router.put('/change_description')
async def change_auction_description(id: int, new_description: str):
    auction_description = change_auction_description_db(id=id, new_description=new_description)
    return auction_description


@auction_router.put('/change_starting_bid')
async def change_starting_bid(id: int, new_bid: float):
    starting_bid = change_starting_bid_db(id=id, new_bid=new_bid)
    return starting_bid


@auction_router.put('/change_end_time')
async def change_end_time(id: int, duration: int):
    new_end_time = change_end_time_db(id=id, duration=duration)
    return new_end_time


@auction_router.put('/extend_end_time')
async def extend_end_time(id: int, plus_to_time: int):
    new_end_time = extend_end_time_db(id=id, plus_to_time=plus_to_time)
    return new_end_time


@auction_router.put('/finish_auction')
async def finish_auction(id):
    finish = finish_auction_db(id=id)
    return finish


@auction_router.delete('/delete_auction')
async def delete_auction(id: int):
    delete = delete_auction_db(id=id)
    return delete

@auction_router.delete('/delete_finished_auctions')
async def delete_finished_auction():
    delete = delete_finished_auction_db()
    return delete