from utils.db import db
from dataclasses import dataclass
from sqlalchemy import TIMESTAMP
from sqlalchemy.sql import func

@dataclass
class Consignation(db.Model):
    __tablename__ = 'consignation'
    id : int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date: TIMESTAMP = db.Column(db.TIMESTAMP(timezone=False), nullable=False, server_default=func.now())
    fundament: str = db.Column(db.String(255), nullable=False)
    observation: str = db.Column(db.String(255), nullable=False)
    id_diagnosis: int = db.Column(db.Integer, db.ForeignKey('diagnosis.id'), nullable=False)
    id_patient: int = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    id_resolved_test: int = db.Column(db.Integer, db.ForeignKey('resolved_test.id'), nullable=False)
    id_specialist: int = db.Column(db.Integer, db.ForeignKey('specialist.id'), nullable=False)
    id_treatment: int = db.Column(db.Integer, db.ForeignKey('treatment.id'), nullable=False)

    def __init__(self, fundament, observation, id_diagnosis, id_patient, id_resolved_test, id_specialist, id_treatment):
        self.fundament = fundament
        self.observation = observation
        self.id_diagnosis = id_diagnosis
        self.id_patient = id_patient
        self.id_resolved_test = id_resolved_test
        self.id_specialist = id_specialist
        self.id_treatment = id_treatment