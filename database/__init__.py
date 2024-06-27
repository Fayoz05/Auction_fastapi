# Импортируем чтобы создавать движок
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Указываем тип БД (Sqlite, Postgres...)
SQLALCHEMY_DATABASE_URI = "sqlite:///auction_api.db"
# Создаем движок
engine = create_engine(SQLALCHEMY_DATABASE_URI)
# Создаем нашу сессию
SessionLocal = sessionmaker(bind=engine)
# Создаем полноценную базу
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()