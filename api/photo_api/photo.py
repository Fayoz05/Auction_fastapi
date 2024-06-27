from fastapi import APIRouter, File, UploadFile, Request, Body
from database.photoservice import *

photo_router = APIRouter(tags=['API for Photos'], prefix='/photos')


@photo_router.get('/get_all_photos')
async def get_all_photos():
    photos = get_all_photos_db()
    return photos


@photo_router.post('/add_photo')
async def add_photo(auction_item_id: int, photo_path: UploadFile = File(...)):
    if photo_path:
        with open(f'api/photo_api/photos/photo_{auction_item_id}.jpg', 'wb') as photo:
            photo_to_save = await photo_path.read()
            photo.write(photo_to_save)
            add_photo_db(auction_item_id, f'api/photo_api/photos/photo_{auction_item_id}.jpg')
        return {'status': 1, 'message': 'Success'}
    else:
        return {'status': 0, 'message': 'Empty'}


@photo_router.delete('/delete_photo')
async def delete_photo(auction_item_id: int):
    delete = delete_photo_db(auction_item_id=auction_item_id)
    return delete
