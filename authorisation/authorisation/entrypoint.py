from .base import NewSession, engine, Base
from sqlalchemy.orm import Session


def main():
    Base.metadata.create_all(engine)

    

if __name__ == '__main__':
    main()