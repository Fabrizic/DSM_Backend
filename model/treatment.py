from utils.db import db
from dataclasses import dataclass

@dataclass
class Treatment(db.Model):
    __tablename__ = 'treatment'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fundament: str = db.Column(db.String(255), nullable=False)
    name: str = db.Column(db.String(65), nullable=False)

    def __init__(self, fundament, name):
        self.fundament = fundament
        self.name = name