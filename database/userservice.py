from database.models import User
from database import get_db
from datetime import datetime, timedelta


def check_user_db(username, phone_number, email):
    db = next(get_db())
    checker_name = db.query(User).filter_by(username=username).first()
    checker_phone = db.query(User).filter_by(phone_number=phone_number).first()
    checker_email = db.query(User).filter_by(email=email).first()
    if checker_name:
        return 'Такой Username уже занят'
    elif checker_phone:
        return 'Такой номер телефона уже занят'
    elif checker_email:
        return 'Такой Email уже занят'
    else:
        return True


def register_user_db(username, phone_number, email, password):
    db = next(get_db())
    checker = check_user_db(username, phone_number, email)
    if checker:
        new_user = User(
            username=username,
            phone_number=phone_number,
            email=email,
            password=password,
            reg_date=datetime.now()
        )
        db.add(new_user)
        db.commit()
        return f'Пользователь {new_user.username} был добавлен'
    else:
        return 'Пользователь с такими данными уже существует'


# Логин
def login_user(email, password):
    db = next(get_db())
    user_email = db.query(User).filter_by(email=email).first()
    print(user_email)
    if user_email:
        if user_email.password == password:
            return user_email
        else:
            return 'Неправильные данные'
    else:
        return 'Нету такого email'


# Изменение email пользователя
def change_user_email_db(id, new_email):
    db = next(get_db())
    user = db.query(User).filter_by(id=id).first()
    if user:
        if user.email == new_email:
            return 'Этот адрес электронной почты уже используется'
        else:
            user.email = new_email
            db.commit()
            return 'Email успешно изменен'
    return False


# Изменение password пользователя
def change_user_password_db(id, new_password):
    db = next(get_db())
    user = db.query(User).filter_by(id=id).first()
    if user:
        if user.password == new_password:
            return 'Этот пароль уже используется'
        else:
            user.password = new_password
            db.commit()
            return 'Пароль успешно изменен'
    return False


# Удаление пользователя logout
def delete_user_db(id):
    db = next(get_db())
    user = db.query(User).filter_by(id=id).first()
    if user:
        db.delete(user)
        db.commit()
        return f'Пользователь удален'
    return False


# Получение данных определенного пользователя
def get_profile_db(id):
    db = next(get_db())
    user_info = db.query(User).filter_by(id=id).first()
    if user_info:
        return user_info
    return False


# Получение всех users
def all_users_db():
    db = next(get_db())
    users = db.query(User).all()
    return users
