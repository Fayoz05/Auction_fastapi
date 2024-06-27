from fastapi import APIRouter, Request
from pydantic import BaseModel
from database.userservice import *
from datetime import datetime
from database import get_db
from typing import Optional
from database.models import User


class UserValidator(BaseModel):
    username: str
    phone_number: str
    email: str
    password: str


user_router = APIRouter(prefix="/user", tags=["API for Users"])


# Получить определенного пользователя
@user_router.get('/api/user')
async def get_user(id: int):
    exact_user = get_profile_db(id)
    return exact_user


# Получение всех users
@user_router.get('/api/all_users')
async def get_all_users():
    users = all_users_db()
    return users


# Регистрация
@user_router.post('/api/registration')
async def registration(validator: UserValidator):
    db = next(get_db())
    user_data = dict(validator)
    user_email = user_data.get('email')
    checker = db.query(User).filter_by(email=user_email).first()
    print(f'вроде ошибка {checker}')
    if not checker:
        try:
            reg_user = register_user_db(**user_data)
            print('Success')
            return {'status': 1, 'message': reg_user}
        except Exception as e:
            print('Error')
            return {'status': 0, 'message': 'Invalid email :('}

    else:
        return {'status': 0, 'message': 'Invalid email :('}


# Логин пользователя
@user_router.post('/api/login')
async def login_user_api(email, password):
    user = login_user(email=email, password=password)
    return user


# Изменения email пользователя
@user_router.put('/api/change_email')
async def change_user_email(id: int, new_email: str):
    email = change_user_email_db(id=id, new_email=new_email)
    return email


# Изменения password пользователя
@user_router.put('/api/change_password')
async def change_user_password(id: int, new_password: str):
    password = change_user_password_db(id=id, new_password=new_password)
    return password


# Удаленение пользователя
@user_router.delete('/api/delete_user')
async def delete_user(id: int):
    delete = delete_user_db(id=id)
    return delete
