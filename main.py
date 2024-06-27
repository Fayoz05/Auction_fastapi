from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from database import Base, engine
from api.user_api.users import user_router
from api.auction_api.auction import auction_router
from api.bid_api.bids import bid_router
from api.photo_api.photo import photo_router

Base.metadata.create_all(bind=engine)

SECRET_KEY = 'WE8634nr873y87f89x3mhf3ertyu'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_HOURS = 24

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

app = FastAPI(docs_url='/')

app.include_router(user_router)
app.include_router(auction_router)
app.include_router(bid_router)
app.include_router(photo_router)