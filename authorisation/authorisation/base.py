from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import environ

engine = create_engine(f"postgresql://postgres:postgres@{environ.get('POSTGRES_URL', 'localhost:5432')[1:-1]}/auth_db")
NewSession = sessionmaker(bind=engine)

Base = declarative_base()