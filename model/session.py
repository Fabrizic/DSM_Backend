from utils.db import db
from datetime import datetime
from sqlalchemy import ForeignKey

class Session(db.Model):
    __tablename__ = 'session'
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, ForeignKey("users.id"), nullable=False)
    start_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    end_time = db.Column(db.DateTime, default=datetime.utcnow,nullable=True)

    def __init__(self, id_user):
        self.id_user = id_user