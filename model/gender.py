from utils.db import db
from dataclasses import dataclass

@dataclass
class Gender(db.Model):
    __tablename__ = 'gender'
    id: int = db.Column(db.Integer, primary_key=True)
    gender_character: str = db.Column(db.String(1), nullable=False)

    def __init__(self, gender_character):
        self.gender_character = gender_character
        





