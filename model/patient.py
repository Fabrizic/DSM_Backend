from utils.db import db
from dataclasses import dataclass

@dataclass
class Patient(db.Model):
    __tablename__ = 'patient'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user: int = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, id_user):
        self.id_user = id_user
        