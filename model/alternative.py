from utils.db import db
from dataclasses import dataclass

@dataclass
class Alternative(db.Model):
    __tablename__ = 'alternative'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description: str = db.Column(db.String(255), nullable=False)
    score: int = db.Column(db.Integer, nullable=False)
    id_template_test: int = db.Column(db.Integer, db.ForeignKey('template_test.id'), nullable=False)

    def __init__(self, description, score, id_template_test):
        self.description = description
        self.score = score
        self.id_template_test = id_template_test
