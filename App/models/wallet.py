from sqlalchemy import Column, Integer
from App.database import db

class Wallet(db.Model):
    __tablename__ = 'wallet'
    id = Column(Integer, name="id", primary_key=True, autoincrement=True)
    debit = Column(Integer, name="debit", default=0)
    credit = Column(Integer, name="credit", default=0)
    balance = Column(Integer, name="balance", default=0)
    
    def __init__(self, debit, credit):
        self.debit = debit
        self.credit = credit
        
    def get_json(self) -> dict:
        return {
            "id" : self.id,
            "debit": self.debit,
            "credit": self.credit,
            "balance": self.balance
        }