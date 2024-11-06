from utils.db import db
from dataclasses import dataclass

@dataclass
class Role(db.Model):
    __tablename__ = 'role'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role: str = db.Column(db.String(50), nullable=False)

    def __init__(self, role):
        self.role = role