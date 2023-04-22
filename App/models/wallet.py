from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from App.database import db

class Wallet(db.Model):
    __table__ = 'wallets'
    user = relationship('User', backref='transaction')
    id = Column(Integer, name="id", primary_key=True, autoincrement=True)