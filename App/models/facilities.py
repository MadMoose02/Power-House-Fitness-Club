from sqlalchemy import Column, Integer, String, Date
from App.database import db

class Facility(db.Model):
    __tablename__ = 'facilities'
    id   = Column(Integer, name="id", primary_key=True, autoincrement=True)
    name = Column(String(20), name="name", nullable=False, unique=True)
    desc = Column(String(500), name="description", nullable=False)
    filename = Column(String(20), name="filename", nullable=False)

    def __init__(self, name, desc, filename):
        self.name = name
        self.desc = desc
        self.filename = filename

    def get_json(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.desc,
            'filename': self.filename
        }