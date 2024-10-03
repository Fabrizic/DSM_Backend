from utils.db import db
from dataclasses import dataclass

@dataclass
class Ubigeo(db.Model):
    __tablename__ = 'ubigeo'
    ubigeo: str = db.Column(db.String(6), primary_key=True)
    departament: str = db.Column(db.String(60), nullable=False)
    district: str = db.Column(db.String(60), nullable=False)
    latitude: float = db.Column(db.Float, nullable=False)
    longitude: float = db.Column(db.Float, nullable=False)
    province: str = db.Column(db.String(60), nullable=False)

    def __init__(self, ubigeo, departament, district, latitude, longitude, province):
        self.ubigeo = ubigeo
        self.departament = departament
        self.district = district
        self.latitude = latitude
        self.longitude = longitude
        self.province = province