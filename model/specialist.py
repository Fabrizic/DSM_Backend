from utils.db import db
from dataclasses import dataclass
from sqlalchemy import ForeignKey

@dataclass
class Specialist(db.Model):
    __tablename__ = 'specialist'
    id : int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    license_character: str = db.Column(db.String(10), nullable=False)
    specialty: str = db.Column(db.String(60), nullable=False)
    id_user: int = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)

    def __init__(self, license_character, specialty, id_user):
        self.license_character = license_character
        self.specialty = specialty
        self.id_user = id_user