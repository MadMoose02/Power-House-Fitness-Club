from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from App.database import db

class UserClass(db.Model):
    __tablename__ = "user_class"
    user = relationship('User', backref='classes')
    class_ = relationship('Class', backref='classes')
    id = Column(Integer, name="id", primary_key=True, autoincrement=True)
    user_id = Column(Integer, db.ForeignKey('user.id'), nullable=False)
    class_id = Column(Integer, db.ForeignKey('classes.id'), nullable=False)
    class_name = Column(String(20), name="name", nullable=False, unique=False)
    paid_by_fitcoin = Column(Boolean, name="paid_by_fitcoin", nullable=False, unique=False)

    def __init__(self, user_id, class_id, class_name, paid_by_fitcoin):
        self.user_id = user_id
        self.class_id = class_id
        self.class_name = class_name
        self.paid_by_fitcoin = paid_by_fitcoin
        
    def get_json(self) -> dict:
        return {
            'id': self.id,
            'user_id': self.user_id,
            'class_id': self.class_id,
            'class_name': self.class_name,
            'paid_by_fitcoin': self.paid_by_fitcoin
        }