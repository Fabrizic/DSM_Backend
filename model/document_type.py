from utils.db import db
from dataclasses import dataclass

@dataclass
class DocumentType(db.Model):
    __tablename__ = 'document_type'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    length: int = db.Column(db.Integer, nullable=False)
    type: str = db.Column(db.String(10), nullable=False)

    def __init__(self, length, type):
        self.length = length
        self.type = type