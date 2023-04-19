from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Date
from App.database import db

class User(db.Model, UserMixin):
    id       = Column(Integer, name="user_id", primary_key=True, autoincrement=True)
    username = Column(String(20), name="username", nullable=False, unique=True)
    password = Column(String(120), name="password_hash", nullable=False, unique=False)
    fname    = Column(String(50), name="first_name", nullable=False, unique=False)
    lname    = Column(String(50), name="last_name", nullable=False, unique=False)
    dob      = Column(Date, name="dob", nullable=False, unique=False)
    address  = Column(String(150), name="address", nullable=False, unique=False)
    phone    = Column(String(15), name="phone", nullable=False, unique=False)
    sex      = Column(String(10), name="gender", nullable=False, unique=False)
    email    = Column(String(50), name="email", nullable=False, unique=False)
    package  = None
    image    = None
    emrg_contacts = None

    def __init__(self, username, password, fname, lname, dob, address, phone, sex, email):
        self.username = username
        self.fname    = fname
        self.lname    = lname
        self.dob      = dob
        self.address  = address
        self.phone    = phone
        self.sex      = sex
        self.email    = email
        self.set_password(password)

    def get_json(self) -> dict:
        return {
            'id': self.id,
            'username': self.username,
            'fname': self.fname,
            'lname': self.lname,
            'sex': self.sex,
            'dob': self.dob,
            'phone': self.phone,
            'email': self.email,
            'address': self.address,
            'package': self.package
        }

    def set_password(self, password: str) -> None:
        """Hashes the password parameter and stores within the object"""
        self.password = generate_password_hash(password, method='sha256')
  
    def check_password(self, password: str) -> bool:
        """Check hashed password. Returns true if the parameter is equal to the object's 
        password property"""
        return check_password_hash(self.password, password)