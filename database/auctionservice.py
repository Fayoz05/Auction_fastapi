from database.models import AuctionItem, User
from database import get_db
from datetime import datetime, timedelta


# Получение всех аукционов
def all_auctions_db():
    db = next(get_db())
    auctions = db.query(AuctionItem).all()
    return auctions


# Получение определенного предмета
def get_exact_item_db(id):
    db = next(get_db())
    item = db.query(AuctionItem).filter_by(id=id).first()
    if item:
        return item
    return False


# Создание аукциона
def create_auction_db(user_id, name, description, starting_bid, duration):
    db = next(get_db())
    checker = db.query(User).filter_by(id=user_id).first()
    if checker:
        auction_end_time = datetime.now() + timedelta(hours=duration)
        new_auction = AuctionItem(user_id=user_id, name=name, description=description,
                                  starting_bid=starting_bid, auction_created=datetime.now(),
                                  auction_end_time=auction_end_time)
        db.add(new_auction)
        db.commit()
        return f'Создан новый аукцион с ID {new_auction.id}, окончание аукциона в {auction_end_time}'
    return 'Нет пользователя с таким user_id'


# Изменение названия аукциона
def change_auction_name_db(id, new_name):
    db = next(get_db())
    checker = db.query(AuctionItem).filter_by(id=id).first()
    if checker:
        if checker.name == new_name:
            return f'Название аукциона уже {new_name}'
        else:
            checker.name = new_name
            db.commit()
            return f'Название аукциона изменено на {new_name}'
    return False



# Изменение описания аукциона
def change_auction_description_db(id, new_description):
    db = next(get_db())
    checker = db.query(AuctionItem).filter_by(id=id).first()
    if checker:
        if checker.description == new_description:
            return f'Описание аукциона уже {new_description}'
        else:
            checker.description = new_description
            db.commit()
            return f'Описание аукциона изменено на {new_description}'
    return False


# Изменение начальной ставки
def change_starting_bid_db(id, new_bid):
    db = next(get_db())
    checker = db.query(AuctionItem).filter_by(id=id).first()
    if checker:
        if checker.starting_bid == new_bid:
            return f'Начальная ставка уже {new_bid}'
        else:
            checker.starting_bid = new_bid
            db.commit()
            return f'Начальная ставка изменена на {new_bid}'
    return False


# Изменить время окончания от начала
def change_end_time_db(id, duration):
    db = next(get_db())
    auction = db.query(AuctionItem).filter_by(id=id).first()
    if auction:
        if auction.auction_end_time < datetime.now():
            return 'Аукцион уже завершен'
        else:
            new_end_time = auction.auction_created + timedelta(hours=duration)
            auction.auction_end_time = new_end_time
            db.commit()
            return f'Аукцион с ID {auction.id} завершится в {auction.auction_end_time}'
    return False


# Продлить аукцион от конца времени
def extend_end_time_db(id, plus_to_time):
    db = next(get_db())
    auction = db.query(AuctionItem).filter_by(id=id).first()
    if auction:
        new_end_time = auction.auction_end_time + timedelta(hours=plus_to_time)
        auction.auction_end_time = new_end_time
        db.commit()
        return f'Аукцион с ID {auction.id} завершится в {auction.auction_end_time}'
    return False


# Завершить аукцион
def finish_auction_db(id):
    db = next(get_db())
    auction = db.query(AuctionItem).filter_by(id=id).first()
    if auction:
        if auction.auction_end_time < datetime.now():
            return 'Аукцион уже завершен'
        else:
            auction.auction_end_time = datetime.now()
            db.commit()
            return f'Аукцион с ID {auction.id} завершен сейчас в {auction.auction_end_time}'
    return False


# Удаление аукциона
def delete_auction_db(id):
    db = next(get_db())
    auction = db.query(AuctionItem).filter_by(id=id).first()
    if auction:
        db.delete(auction)
        db.commit()
        return 'Аукцион удален'
    return False

def delete_finished_auction_db():
    db = next(get_db())
    auctions = db.query(AuctionItem).filter(AuctionItem.auction_end_time < datetime.now()).all()
    if auctions:
        for auction in auctions:
            db.delete(auction)
        db.commit()
        return 'Завершенные аукционы удалены :)'
    return False
