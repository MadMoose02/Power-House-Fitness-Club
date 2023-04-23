from sqlalchemy import Column, Integer, String
from App.database import db

class Facility(db.Model):
    __tablename__ = 'facilities'
    id   = Column(Integer, name="id", primary_key=True, autoincrement=True)
    name = Column(String(20), name="name", nullable=False, unique=True)
    desc = Column(String(500), name="description", nullable=False)
    filename = Column(String(20), name="filename", nullable=False)
    package = Column(String(100), name="package", nullable=False)

    def __init__(self, name, desc, filename, package):
        self.name = name
        self.desc = desc
        self.filename = filename
        self.package = package

    def get_json(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.desc,
            'filename': self.filename,
            'package': self.package
        }