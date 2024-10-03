from utils.db import db
from dataclasses import dataclass

@dataclass
class Document_type(db.Model):
    __table__ = 'document_type'
    id: int = db.Column(db.Integer, primary_key=True)
    length: int = db.Column(db.Integer, nullable=False)
    type: str = db.Column(db.String(10), nullable=False)

    def __init__(self, id, length, type):
        self.id = id
        self.length = length
        self.type = type