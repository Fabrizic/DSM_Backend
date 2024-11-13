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

@ubigeo_route.route('/departamentos', methods=['GET'])
def get_departments():
    departments = Ubigeo.query.with_entities(Ubigeo.departament).distinct().all()
    data = {
        'message': 'Todos los departamentos',
        'status': 200,
        'data': [
            {
                'departament': department.departament
            } for department in departments
        ]
    }

    return make_response(jsonify(data), 200)

@ubigeo_route.route('/departamentos/<string:departament', methods=['GET'])
def get_provinces(departament):
    provinces = Ubigeo.query.with_entities(Ubigeo.province).filter_by(departament=departament).distinct().all()
    data = {
        'message': 'Todas las provincias',
        'status': 200,
        'data': [
            {
                'province': province.province
            } for province in provinces
        ]
    }

    return make_response(jsonify(data), 200)

@ubigeo_route.route('/departamentos/<string:departament>/provincias/<string:province>', methods=['GET'])
def get_districts(departament, province):
    districts = Ubigeo.query.with_entities(Ubigeo.district).filter_by(departament=departament, province=province).distinct().all()
    data = {
        'message': 'Todos los distritos',
        'status': 200,
        'data': [
            {
                'district': district.district
            } for district in districts
        ]
    }

    return make_response(jsonify(data), 200)