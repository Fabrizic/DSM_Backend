from sqlalchemy import Date, ForeignKey
from utils.db import db
from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash

@dataclass
class Person(db.Model):
    __tablename__ = 'person'
    document_character: str = db.Column(db.String(10), primary_key=True)
    birth_date: Date = db.Column(db.Date, nullable=False)
    email: str = db.Column(db.String(60), nullable=False)
    last_name: str = db.Column(db.String(60), nullable=False)
    name: str = db.Column(db.String(60), nullable=False)
    phone: str = db.Column(db.String(15), nullable=False)
    second_last_name: str = db.Column(db.String(60), nullable=False)
    document_type: int = db.Column(db.Integer, ForeignKey('document_type.id'), nullable=False)  
    gender: int = db.Column(db.Integer, ForeignKey('gender.id'),nullable=False)
    ubigeo: str = db.Column(db.String(6), ForeignKey('ubigeo.ubigeo'), nullable=False) 

    def __init__(self, document_character, birth_date, email, last_name, name, phone, second_last_name, document_type, gender, ubigeo):
        self.document_character = document_character
        self.birth_date = birth_date
        self.email = email
        self.last_name = last_name
        self.name = name
        self.phone = phone
        self.second_last_name = second_last_name
        self.document_type = document_type
        self.gender = gender
        self.ubigeo = ubigeo         

