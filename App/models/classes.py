from sqlalchemy import Column, Integer, String, Date
from App.database import db

class Class(db.Model):
    id         = Column(Integer,name="class_id", primary_key=True, autoincrement=True)
    instructor = Column(String(20), name="instructor", nullable=False, unique=False)
    desc       = Column(String(500), name="description", nullable=False, unique=False)

    def __init__(self, instructor, desc):
        self.instructor = instructor
        self.desc = desc
        
    def get_json(self) -> dict:
        return {
            'id': self.id,
            'instructor': self.instructor,
            'description': self.desc
        }