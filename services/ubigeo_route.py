from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.ubigeo import Ubigeo

ubigeo_route = Blueprint('ubigeo_route', __name__)

@ubigeo_route.route('/ubigeo', methods=['GET'])
def get_ubigeo():
    ubigeo = Ubigeo.query.all()
    data = {
        'message': 'Todos los ubigeos',
        'status': 200,
        'data': [
            {
                'ubigeo': ubigeo.ubigeo,
                'departament': ubigeo.departament,
                'province': ubigeo.province,
                'district': ubigeo.district
            } for ubigeo in ubigeo
        ]
    }

    return make_response(jsonify(data), 200)