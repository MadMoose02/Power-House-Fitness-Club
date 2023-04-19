from sqlalchemy import Column, Integer, String, Date
from App.database import db

class Facility(db.Model):
    id   = Column(Integer, name="faciltiy_id", primary_key=True, autoincrement=True)
    name = Column(String(20), name="name", nullable=False, unique=True)
    desc = Column(String(500), name="description", nullable=False)

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def get_json(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.desc
        }