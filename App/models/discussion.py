from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from App.database import db

class Discussion(db.Model):
    __tablename__ = 'discussion'
    users = relationship('User', backref='discussion', cascade="all, delete")
    id = Column(Integer, name="id", primary_key=True, autoincrement=True)
    title = Column(String(100), name="title", nullable=False, unique=True)
    started_by = Column(Integer, db.ForeignKey('user.id'), nullable=False)
    
    
    def __init__(self, title, started_by):
        self.title = title
        self.started_by = started_by
        
        
    def get_json(self) -> dict:
        return {
            "id" : self.id,
            "title": self.title,
            "started_by": self.started_by
        }