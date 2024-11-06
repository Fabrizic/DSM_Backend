from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.users import Users

login_route = Blueprint('login_route', __name__)

@login_route.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    role = request.json['role']

    login = Users.query.filter_by(username=username, role=role).first()

    if login and login.check_password(password):
        data = {
            'message': 'Login successful',
            'status': 200,
            'data': {
                'id': login.id,
                'username': login.username,
                'role': login.role
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
    return jsonify([login.serialize() for login in logins])

@login_route.route('/login/<int:id>', methods=['GET'])
def get_login(id):
    login = Users.query.get(id)
    return jsonify(login.serialize())

