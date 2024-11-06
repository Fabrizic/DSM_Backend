from utils.db import db
from dataclasses import dataclass

@dataclass
class Emotion(db.Model):
    __tablename__ = 'emotion'
    id: int = db.Column(db.Integer ,primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(50), nullable=False)

    def __init__(self,name):
        self.name = name