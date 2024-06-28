from database.models import Bid, AuctionItem, User
from database import get_db
from datetime import datetime, timedelta


# Назначить ставку
def make_bid_db(user_id, auction_item_id, bid_amount):
    db = next(get_db())
    # Проверка наличия пользователя
    user = db.query(User).filter_by(id=user_id).first()
    if user:
        # Проверка наличия аукционного предмета
        auction_item = db.query(AuctionItem).filter_by(id=auction_item_id).first()
        if auction_item:
            # Проверка, что пользователь не делает ставку на свой аукцион
            if auction_item.user_id != user_id:
                # Проверка, что аукцион не завершился
                current_time = datetime.now()
                if current_time > auction_item.auction_end_time:
                    return 'Аукцион уже завершен'
                else:
                    # Проверка наличия ставки этого пользователя на этот аукционный предмет
                    existing_bid = db.query(Bid).filter_by(user_id=user_id, auction_item_id=auction_item_id).first()
                    if existing_bid:
                        if auction_item.starting_bid <= bid_amount:
                            # Если ставка уже существует, обновляем её bid_amount
                            existing_bid.bid_amount = bid_amount
                            db.commit()
                            return f'Сумма ставки обновлена до {bid_amount} для аукционного предмета с ID {auction_item_id}'
                        else:
                            return f'Вы не можете поставить {bid_amount} так как ставки начинаются с {auction_item.starting_bid}'
                    else:
                        if auction_item.starting_bid <= bid_amount:
                            # Создание ставки
                            bid = Bid(user_id=user_id, auction_item_id=auction_item_id, bid_amount=bid_amount)
                            db.add(bid)
                            db.commit()
                            return f'Ставка {bid_amount} принята по предмету с ID {auction_item_id}'
                        else:
                            return f'Вы не можете поставить {bid_amount} так как ставки начинаются с {auction_item.starting_bid}'
            return 'Вы не можете сделать ставку на свой аукцион'
        return 'Аукционный предмет с предоставленным auction_item_id не найден'
    return 'Пользователь с предоставленным user_id не найден'


# Получить все ставки
def get_all_bids_db():
    db = next(get_db())
    bids = db.query(Bid).all()
    return bids


# Увеличить ставку на определенную сумму
def greater_bid_db(user_id, auction_item_id, plus_bid):
    db = next(get_db())
    existing_bid = db.query(Bid).filter_by(user_id=user_id, auction_item_id=auction_item_id).first()
    if existing_bid:
        existing_bid.bid_amount += plus_bid
        db.commit()
        return f'Ваша ставка увеличилась на {plus_bid} и теперь она {existing_bid.bid_amount}'
    return 'Вы не создали ставку так что не можете ее увеличить'


# Уменьшить ставку на определенную сумму
def lower_bid_db(user_id, auction_item_id, minus_bid):
    db = next(get_db())
    existing_bid = db.query(Bid).filter_by(user_id=user_id, auction_item_id=auction_item_id).first()
    auction_item = db.query(AuctionItem).filter_by(id=auction_item_id).first()
    if existing_bid:
        auction_item = db.query(AuctionItem).filter_by(id=auction_item_id).first()
        existing_bid.bid_amount -= minus_bid
        if existing_bid.bid_amount < auction_item.starting_bid:
            return f'Ваше уменьшение ставки не валидна'
        else:
            db.commit()
            return f'Ваша ставка уменьшилась на {minus_bid} и теперь она {existing_bid.bid_amount}'
    return 'Вы не создали ставку так что не можете ее уменьшить'


# Сортировать ставки по убыванию
def sort_bids_db(auction_item_id: int):
    db = next(get_db())
    existing_bids = db.query(Bid).filter_by(auction_item_id=auction_item_id).order_by(Bid.bid_amount.desc()).all()
    new = []
    for i in existing_bids:
        new.append(
            {
                "user_id": i.user_id,
                "bid_amount": i.bid_amount
            }
        )
    return new[:5]


# Удалить ставку по id
def delete_bid_db(id, user_id, auction_item_id: int):
    db = next(get_db())
    checker = db.query(Bid).filter_by(id=id, user_id=user_id, auction_item_id=auction_item_id).first()
    if checker:
        db.delete(checker)
        db.commit()
        return f'Ставка по id {id} была удалена'
    return 'Нет такой ставки'


# Удалить все ставки user
def delete_user_bids_db(user_id):
    db = next(get_db())
    checker = db.query(Bid).filter_by(user_id=user_id).all()
    if checker:
        for bid in checker:
            db.delete(bid)
            db.commit()
        return f'Ставки user {user_id} были удалены'
    return f'У user {user_id} не было ставок'
