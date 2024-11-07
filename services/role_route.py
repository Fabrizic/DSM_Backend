from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.role import Role

role_route = Blueprint('role_route', __name__)

@role_route.route('/role', methods=['GET'])
def get_roles():
    roles = Role.query.all()
    data = {
        'message': 'Todos los roles',
        'status': 200,
        'data': [
            {
                'id': role.id,
                'role': role.role
            } for role in roles
        ]
    }

    return make_response(jsonify(data), 200)

@role_route.route('/role', methods=['POST'])
def create_role():
    role = request.json['role']

    new_role = Role(
        role=role
    )

    db.session.add(new_role)
    db.session.commit()

    data = {
        'message': 'Rol creado',
        'status': 200,
        'data': {
            'id': new_role.id,
            'role': new_role.role
        }
    }

    return make_response(jsonify(data), 200)
