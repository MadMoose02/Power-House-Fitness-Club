from sqlalchemy import Column, Integer, String, Date
from App.database import db

class Package(db.Model):
    id = Column(Integer,primary_key=True)
    package_type = Column(String,nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String, nullable=False)

    def __init__(self,package_type,price,description):
        self.package_type = package_type
        self.price = price
        self.description = description

    def get_json(self) -> Dict[str, str]:
        return {
            "id": str(self.id),
            "package_type": self.package_type,
            "price": str(self.price),
            "description": self.description
        }