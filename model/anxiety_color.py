from utils.db import db
from dataclasses import dataclass

@dataclass
class Anxiety_color(db.Model):
    __tablename__ = 'anxiety_color'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    color: str = db.Column(db.String(255), nullable=False)

    def __init__(self, color, description):
        self.color = color
        self.description = description