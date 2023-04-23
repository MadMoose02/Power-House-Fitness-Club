from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Date, LargeBinary
from sqlalchemy.orm import relationship
from App.database import db

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    package = relationship('Package', backref='user')
    emrg_contact = relationship('EmergencyContact', backref='user')
    wallet = relationship('Wallet', backref='user')
    id = Column(Integer, name="id", primary_key=True, autoincrement=True)
    username = Column(String(20), name="username", nullable=False, unique=True)
    password = Column(String(120), name="password_hash", nullable=False, unique=False)
    fname = Column(String(50), name="first_name", nullable=False, unique=False)
    lname = Column(String(50), name="last_name", nullable=False, unique=False)
    dob = Column(Date, name="dob", nullable=False, unique=False)
    address = Column(String(150), name="address", nullable=False, unique=False)
    phone = Column(String(15), name="phone", nullable=False, unique=False)
    sex = Column(String(10), name="gender", nullable=False, unique=False)
    email = Column(String(50), name="email", nullable=False, unique=False)
    image = Column(LargeBinary, name="image", nullable=False, unique=False)
    package_id = Column(Integer, db.ForeignKey('package.id'), nullable=False)
    emergency_contact_id = Column(Integer, db.ForeignKey('emergency_contact.id'), nullable=False)
    wallet_id = Column(Integer, db.ForeignKey('wallet.id'), nullable=False)

    def __init__(self, username, password, fname, lname, dob, address, phone, 
                 sex, email, image, package_id, emergency_contact_id, wallet_id):
        self.username = username
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.address = address
        self.phone = phone
        self.sex = sex
        self.email = email
        self.image = image
        self.package_id = package_id
        self.emergency_contact_id = emergency_contact_id
        self.wallet_id = wallet_id
        self.set_password(password)

    def get_json(self) -> dict:
        return {
            'id': self.id,
            'username': self.username,
            'fname': self.fname,
            'lname': self.lname,
            'dob': self.dob,
            'address': self.address,
            'phone': self.phone,
            'sex': self.sex,
            'email': self.email,
            'package_id': self.package_id,
            'emergency_contact_id': self.emergency_contact_id,
            'wallet_id' : self.wallet_id
        }

    def set_password(self, password: str) -> None:
        """Hashes the password parameter and stores within the object"""
        self.password = generate_password_hash(password, method='sha256')
  
    def check_password(self, password: str) -> bool:
        """Check hashed password. Returns true if the parameter is equal to the object's 
        password property"""
        return check_password_hash(self.password, password)