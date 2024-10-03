from utils.db import db
from dataclasses import dataclass

@dataclass
class Answer(db.Model):
    __tablename__ = 'answer'
    id : int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_alternative: int = db.Column(db.Integer, db.ForeignKey('alternative.id'), nullable=False)
    id_question: int = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    id_resolved_test: int = db.Column(db.Integer, db.ForeignKey('resolved_test.id'), nullable=False)

    def __init__(self, id_alternative, id_question, id_resolved_test):
        self.id_alternative = id_alternative
        self.id_question = id_question
        self.id_resolved_test = id_resolved_test