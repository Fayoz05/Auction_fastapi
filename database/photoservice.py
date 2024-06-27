from database import get_db
from database.models import AuctionPhoto
from datetime import datetime
import os

# Загрузка изображений для поста
def add_photo_db(auction_item_id, photo_path):
    db = next(get_db())
    photo = AuctionPhoto(auction_item_id=auction_item_id, photo_path=photo_path, reg_date=datetime.now())
    db.add(photo)
    db.commit()
    return f'Фото успешно добавлено для предмета с id {auction_item_id}'


# Вернуть все изображения
def get_all_photos_db():
    db = next(get_db())
    all_photos = db.query(AuctionPhoto).all()
    return all_photos

# Удаление изображения по item_id
def delete_photo_db(auction_item_id: int):
    db = next(get_db())
    photos = db.query(AuctionPhoto).filter_by(auction_item_id=auction_item_id).all()
    if photos:
        for photo in photos:
            photo_path = photo.photo_path
            if os.path.exists(photo_path):
                os.remove(photo_path)  # Удаление файла с диска
            db.delete(photo)
        db.commit()
        return f'Фото для предмета с id {auction_item_id} успешно удалены'
    return f'Фото для предмета с id {auction_item_id} не найдены'