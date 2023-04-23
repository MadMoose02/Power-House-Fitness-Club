from sqlalchemy import Column, Integer, String
from App.database import db

class Class(db.Model):
    __tablename__ = "classes"
    id         = Column(Integer, name="id", primary_key=True, autoincrement=True)
    name       = Column(String(20), name="name", nullable=False, unique=False)
    instructor = Column(String(20), name="instructor", nullable=False, unique=False)
    desc       = Column(String(500), name="description", nullable=False, unique=False)
    filename   = Column(String(20), name="filename", nullable=False, unique=False)

    def __init__(self, name, instructor, desc, filename):
        self.name = name
        self.instructor = instructor
        self.desc = desc
        self.filename = filename
        
    def get_json(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'instructor': self.instructor,
            'description': self.desc,
            'filename': self.filename
        }