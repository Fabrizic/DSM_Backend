from utils.db import db
from dataclasses import dataclass
from sqlalchemy import TIMESTAMP, func

@dataclass
class Emotion_detection(db.Model):
    __tablename__ = 'emotion_detection'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user: int = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    id_emotion: int = db.Column(db.Integer, db.ForeignKey('emotion.id'), nullable=False)
    id_session: int = db.Column(db.Integer, db.ForeignKey('session.id'), nullable=False)
    detection_time: TIMESTAMP = db.Column(db.TIMESTAMP(timezone=False), nullable=False, server_default=func.now())
    confidence: float = db.Column(db.Float, nullable=False)

    def __init__(self, id_user, id_emotion, confidence):
        self.id_user = id_user
        self.id_emotion = id_emotion
        self.confidence = confidence