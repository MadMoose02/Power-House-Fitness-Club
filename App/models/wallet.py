from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from App.database import db

class Wallet(db.Model):
    __tablename__ = 'wallet'
    user = relationship('User', backref='wallet', cascade="all, delete")
    id = Column(Integer, name="id", primary_key=True, autoincrement=True)
    user_id = Column(Integer, db.ForeignKey('user.id'), nullable=False, unique=True)
    debit = Column(Integer, name="debit", default=0)
    credit = Column(Integer, name="credit", default=0)
    
    def __init__(self, user_id, debit, credit):
        self.user_id = user_id
        self.debit = debit
        self.credit = credit
        
    def get_json(self) -> dict:
        return {
            "user_id": self.user_id,
            "debit": self.debit,
            "credit": self.credit
        }