from utils.db import db
from dataclasses import dataclass

@dataclass
class Template_test:
    __tablename__ = 'template_test'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author: str = db.Column(db.String(65), nullable=False)
    description: str = db.Column(db.String(255), nullable=False)
    name: str = db.Column(db.String(65), nullable=False)

    def __init__(self, author, description, name):
        self.author = author
        self.description = description
        self.name = name