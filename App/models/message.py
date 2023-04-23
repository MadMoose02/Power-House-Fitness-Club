from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from App.database import db

class Message(db.Model):
    __tablename__ = 'message'
    id = Column(Integer, name="id", primary_key=True, autoincrement=True)
    discussion = relationship('Discussion', backref='message', cascade="all, delete")
    discussion_id = Column(Integer, db.ForeignKey('discussion.id'), nullable=False)
    user_id = Column(Integer, db.ForeignKey('user.id'), nullable=False)
    content = Column(String(500), name="content", nullable=False)
    datetime = Column(String(20), name="datetime", nullable=False)
    
    
    def __init__(self, discussion_id, user_id, content, datetime):
        self.discussion_id = discussion_id
        self.user_id = user_id
        self.content = content
        self.datetime = datetime
        
        
    def get_json(self) -> dict:
        return {
            "id" : self.id,
            "discussion_id": self.discussion_id,
            "user_id": self.user_id,
            "content": self.content,
            "datetime": self.datetime
        }