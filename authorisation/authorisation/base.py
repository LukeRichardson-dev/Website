from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import environ

pg_address = f"postgresql://postgres:postgres@{environ.get('POSTGRES_URL', 'localhost:5432')}/auth_db"
print(pg_address)
engine = create_engine(pg_address)
NewSession = sessionmaker(bind=engine)

Base = declarative_base()