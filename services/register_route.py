from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.person import Person
from model.users import Users
from model.ubigeo import Ubigeo
from model.document_type import DocumentType
from model.gender import Gender

register_route = Blueprint('register_route', __name__)

@register_route.route('/register', methods=['POST'])
def create_register():
    document_type = request.json['document_type']
    document_character = request.json['document_character']
    birth_date = request.json['birth_date']
    email = request.json['email']
    name = request.json['name']
    last_name = request.json['last_name']
    second_last_name = request.json['second_last_name']
    gender = request.json['gender']
    phone = request.json['phone']
    department = request.json['department']
    province = request.json['province']
    district = request.json['district']
    username = request.json['username']
    password = request.json['password']
    role = request.json['role']

    gender = Gender.query.filter_by(gender_character=gender).first()
    document_type = DocumentType.query.filter_by(type=document_type).first()
    ubigeo = Ubigeo.query.filter_by(departament=department, province=province, district=district).first()

    if ubigeo:
        ubigeo = ubigeo.ubigeo
    else:
        ubigeo = None
    
    new_person = Person(
        document_character=document_character,
        birth_date=birth_date,
        email=email,
        last_name=last_name,
        name=name,
        phone=phone,
        second_last_name=second_last_name,
        document_type=document_type.id,
        gender=gender.id,
        ubigeo=ubigeo
    )

    db.session.add(new_person)
    db.session.flush()

    new_user = Users(
        password=password,
        role=role,
        username=username,
        id_person=document_character
    )

    db.session.add(new_user)
    db.session.commit()

    data = {
        'message': 'Register created',
        'status': 201,
        'data': {
            'document_character': new_person.document_character,
            'birth_date': new_person.birth_date,
            'email': new_person.email,
            'last_name': new_person.last_name,
            'name': new_person.name,
            'phone': new_person.phone,
            'second_last_name': new_person.second_last_name,
            'document_type': new_person.document_type,
        }
    }

    return make_response(jsonify(data), 201)

@register_route.route('/registers', methods=['GET'])
def get_registers():
    registers = Person.query.all()
    data = {
        'message': 'Registers fetched',
        'status': 200,
        'data': []
    }

    for register in registers:
        data['data'].append({
            'document_character': register.document_character,
            'birth_date': register.birth_date,
            'email': register.email,
            'last_name': register.last_name,
            'name': register.name,
            'phone': register.phone,
            'second_last_name': register.second_last_name,
            'document_type': register.document_type,
            'gender': register.gender
        })
    



