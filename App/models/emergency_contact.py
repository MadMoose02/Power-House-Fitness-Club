from sqlalchemy import Column, Integer, String
from App.database import db

class EmergencyContact(db.Model):
    __tablename__ = 'emergency_contact'
    id       = Column(Integer, name="id", primary_key=True, autoincrement=True)
    fname    = Column(String(50), name="first_name", nullable=False, unique=False)
    lname    = Column(String(50), name="last_name", nullable=False, unique=False)
    relation = Column(String(20), name="relationship", nullable=False, unique=False)
    contact  = Column(String(15), name="contact", nullable=False, unique=False)

    def __init__(self, fname, lname, relation, contact):
        self.fname    = fname
        self.lname    = lname
        self.relation = relation
        self.contact  = contact

    def get_json(self) -> dict:
        return {
            'id': self.id,
            'fname': self.fname,
            'lname': self.lname,
            'relationship': self.relation,
            'contact': self.contact
        }