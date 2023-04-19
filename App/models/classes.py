from sqlalchemy import Column, Integer, String, Date
from App.database import db

class Class(db.Model):
    id    =Coloumn(Integer,name="class_id", primary_key=True, autoincrement=True)
    inst_name   =Column(String, name="instName", nullable=False, unique=False)
    descript    =Column(String, name="classDescription", nullable=False, unique=False)

