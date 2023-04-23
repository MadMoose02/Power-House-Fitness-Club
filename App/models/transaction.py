from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from App.database import db

class Transaction(db.Model):
    __tablename__ = 'transaction'
    user = relationship('User', backref='transaction', cascade="all, delete")
    wallet = relationship('Wallet', backref='transaction', cascade="save-update, delete")
    id = Column(Integer, name="id", primary_key=True, autoincrement=True)
    user_id = Column(Integer, db.ForeignKey('user.id'), nullable=False)
    wallet_id = Column(Integer, db.ForeignKey('wallet.id'), nullable=False)
    details = Column(String(150), name="details", nullable=False)
    datetime = Column(DateTime, name="date", nullable=False)
    
    
    def __init__(self, user_id, wallet_id, details, datetime) -> dict:
        self.user_id = user_id
        self.wallet_id = wallet_id
        self.details = details
        self.datetime = datetime
        
        
    def get_json(self) -> dict:
        return {
            'id': self.id,
            'user_id': self.user_id,
            'wallet_id': self.wallet_id,
            'details': self.details,
            'datetime': self.datetime
        }