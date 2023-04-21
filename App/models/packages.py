from sqlalchemy import Column, Integer, String
from App.database import db

class Package(db.Model):
    __tablename__ = 'packages'
    id = Column(Integer, name="id", primary_key=True, autoincrement=True)
    type = Column(String(20), name="type", nullable=False)
    price = Column(String(10), name="price", nullable=False)
    desc = Column(String(500), name="description", nullable=False)

    def __init__(self, type, price, desc):
        self.type = type
        self.price = price
        self.desc = desc

    def get_json(self) -> dict:
        return {
            "id": self.id,
            "type": self.type,
            "price": self.price,
            "description": self.desc
        }