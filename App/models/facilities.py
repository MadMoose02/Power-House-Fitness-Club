from sqlalchemy import Column, Integer, String, Date
from App.database import db

class Facility(db.Model):
    id = Column(Integer, autoincrement=True)
    name = Coloumn(String, nullable=False, unique=False)
    description = Column(String(120),nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_jason(self) -> dict:
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description
        }