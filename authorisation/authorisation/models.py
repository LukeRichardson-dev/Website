from sqlalchemy import Column, ForeignKey, String, Integer, Date, Binary
from sqlalchemy.orm import relationship

from base import Base


class Account(Base):

    __tablename__ = 'account'

    account_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(30), unique=True)

    password = Column(Binary)
    salt = Column(Binary)

    tokens = relationship(
        'Token', 
        cascade='all, delete',
        passive_deletes=True
    )

class Token(Base):

    __tablename__ = 'token'
    
    token = Column(Binary, primary_key=True)
    owner_id = Column(Integer, ForeignKey('owner.id', ondelete='CASCADE'))
    owner = relationship('Account', back_populates='tokens')
