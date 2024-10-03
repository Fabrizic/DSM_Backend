from utils.db import db
from dataclasses import dataclass
from sqlalchemy import TIMESTAMP

@dataclass
class Resolved_test(db.Model):
    __tablename__ = 'resolved_test'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date: TIMESTAMP = db.Column(db.TIMESTAMP(timezone=False), nullable=False)
    result: int = db.Column(db.Integer, nullable=False)
    id_classification: int = db.Column(db.Integer, db.ForeignKey('classification.id'), nullable=False)
    id_consignation: int = db.Column(db.Integer, db.ForeignKey('consignation.id'), nullable=False)
    id_patient: int = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    id_template_test: int = db.Column(db.Integer, db.ForeignKey('template_test.id'), nullable=False)

    def __init__(self, date, result, id_classification, id_consignation, id_patient, id_template_test):
        self.date = date
        self.result = result
        self.id_classification = id_classification
        self.id_consignation = id_consignation
        self.id_patient = id_patient
        self.id_template_test = id_template_test