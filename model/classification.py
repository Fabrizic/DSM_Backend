from utils.db import db
from dataclasses import dataclass

@dataclass
class Classification(db.Model):
    __tablename__ = 'classification'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    intensity: int = db.Column(db.Integer, nullable=False)
    interpretation: str = db.Column(db.String(255), nullable=False)
    maximum: int = db.Column(db.Integer, nullable=False)
    minimum: int = db.Column(db.Integer, nullable=False)
    id_color: int = db.Column(db.Integer, db.ForeignKey('anxiety_color.id'), nullable=False)
    id_template_test: int = db.Column(db.Integer, db.ForeignKey('template_test.id'), nullable=False)

    def __init__(self, intensity, interpretation, maximum, minimum, id_color, id_template_test):
        self.intensity = intensity
        self.interpretation = interpretation
        self.maximum = maximum
        self.minimum = minimum
        self.id_color = id_color
        self.id_template_test = id_template_test