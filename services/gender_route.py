from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.gender import Gender

gender_route = Blueprint('gender_route', __name__)

# Create
@gender_route.route('/gender', methods=['POST'])
def create_gender():
    gender_character = request.json[gender_character]

    gender = Gender(gender_character)
    db.session.add(gender)
    db.session.commit()

    if not gender:
        data = {
            'message': 'No se pudo crear el género',
            'status': 400,
            'data': {}
        }

        return make_response(jsonify(data), 400)


    data = {
        'message': 'Género creado',
        'status': 201,
        'data': {
            'id': gender.id,
            'gender_character' : gender.gender_character
        }
    }

    return make_response(jsonify(data), 201)

@gender_route.route('/gender', methods=['GET'])
def get_genders():
    genders = Gender.query.all()
    data = {
        'message': 'Todos los genders',
        'status': 200,
        'data': [
            {
                'id': gender.id,
                'gender_character' : gender.gender_character
            } for gender in genders
        ]
    }


    return make_response(jsonify(data), 200)


