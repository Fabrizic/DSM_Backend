from sqlalchemy import Date, ForeignKey
from utils.db import db
from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash

@dataclass
class Users(db.Model):
    __tablename__ = 'users'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    password: str = db.Column(db.String(128), nullable=False)
    role : int = db.Column(db.Integer, ForeignKey('role.id'), nullable=False)
    username: str = db.Column(db.String(20), nullable=False)
    id_person: str = db.Column(db.String(10), ForeignKey('person.document_character'), nullable=False)

    def __init__(self, password, role, username, id_person):
        self.password = generate_password_hash(password)
        self.role = role
        self.username = username
        self.id_person = id_person

