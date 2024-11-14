from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.users import Users
from model.person import Person

login_route = Blueprint('login_route', __name__)

@login_route.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    role = request.json['role']

    login = Users.query.filter_by(username=username, role=role).first()
    person = Person.query.filter_by(document_character=login.id_person).first()

    if login and login.check_password(password):
        data = {
            'message': 'Login successful',
            'status': 200,
            'data': {
                'username': login.username,
                'id_person': login.id_person,
                'userName': person.name + ' ' + person.last_name
            }
        }

        return make_response(jsonify(data), 200)
    
    data = {
        'message': 'Correo o contraseña incorrectos',
        'status': 400,
        'data': {}
    }

    return make_response(jsonify(data), 400)

@login_route.route('/logins', methods=['GET'])
def get_logins():
    logins = Users.query.all()
    data = {
        'message': 'All logins',
        'status': 200,
        'data': [
            {
                'id': login.id,
                'username': login.username,
                'id_person': login.id_person
            } for login in logins
        ]
    }

    return make_response(jsonify(data), 200)

@login_route.route('/login/<int:id>', methods=['GET'])
def get_login(id):
    login = Users.query.get(id)
    return jsonify(login.serialize())

@login_route.route('/person/<string:document_character>', methods=['GET'])
def get_person(document_character):
    person = Person.query.get(document_character)

    if person is None:
        data = {
            'message': 'Person not found',
            'status': 404,
            'data': {}
        }

        return make_response(jsonify(data), 404)

    data = {
        'message': 'Person fetched',
        'status': 200,
        'data': {
            'userName': person.name + ' ' + person.last_name
        }
    }

    return make_response(jsonify(data), 200)
