from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()
# Получение данных о подключении к базе данных из переменных окружения
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Создание движка для подключения к базе данных PostgreSQL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Создание фабрики сессий для взаимодействия с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создание базового класса для всех моделей
Base = declarative_base()
