from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from App.database import db

class Transaction(db.Model):
    __table__ = 'transactions'
    user = relationship('User', backref='transaction')
    id = Column(Integer, name="id", primary_key=True, autoincrement=True)