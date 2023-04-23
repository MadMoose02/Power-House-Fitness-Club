from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import relationship
from App.database import db

class Activity(db.Model):
    __tablename__ = 'activity'
    user = relationship('User', backref='activity', cascade="all, delete")
    id = Column(Integer, name="id", primary_key=True, autoincrement=True)
    user_id = Column(Integer, db.ForeignKey('user.id'), nullable=False, unique=True)
    date = Column(Date, name="date", nullable=False)
    pre_workout = Column(Boolean, name="pre_workout", default=False)
    energy_level = Column(String(20), name="energy_level", default=False)
    details = Column(String(150), name="details", nullable=False)
    
    
    def __init__(self, user_id, date, pre_workout, energy_level, details) -> dict:
        self.user_id = user_id
        self.date = date
        self.pre_workout = pre_workout
        self.energy_level = energy_level
        self.details = details
        
        
    def get_json(self) -> dict:
        return {
            'id' : self.id,
            'user_id' : self.user_id,
            'date' : self.date,
            'pre_workout' : self.pre_workout,
            'energy_level' : self.energy_level,
            'details' : self.details
        }