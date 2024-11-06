from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.emotion import Emotion

emotion_route = Blueprint('emotion_route', __name__)

@emotion_route.route('/emotion', methods=['POST'])
def create_emotion():
    name = request.json['name']
    emotion = Emotion(name)
    db.session.add(emotion)
    db.session.commit()
    
    if not emotion:
        data = { 
            'message': 'Emotion not created' ,
            'status': 400,
            'data': {}
        }

        return make_response(jsonify(data), 400)
    
    data = {
        'message': 'Emotion created',
        'status': 201,
        'data': {
            'id': emotion.id,
            'name': emotion.name
        }
    }

    return make_response(jsonify(data), 201)

@emotion_route.route('/emotion', methods=['GET'])
def get_emotions():
    emotions = Emotion.query.all()
    data = {
        'message': 'Emotions fetched',
        'status': 200,
        'data': []
    }

    for emotion in emotions:
        data['data'].append({
            'id': emotion.id,
            'name': emotion.name
        })

    return make_response(jsonify(data), 200)

@emotion_route.route('/emotion/<int:id>', methods=['GET'])
def get_emotion(id):
    emotion = Emotion.query.get(id)
    data = {
        'message': 'Emotion fetched',
        'status': 200,
        'data': {
            'id': emotion.id,
            'name': emotion.name
        }
    }

    return make_response(jsonify(data), 200)

@emotion_route.route('/emotion/<int:id>', methods=['PUT'])
def update_emotion(id):
    emotion = Emotion.query.get(id)
    emotion.name = request.json['name']
    db.session.commit()
    data = {
        'message': 'Emotion updated',
        'status': 200,
        'data': {
            'id': emotion.id,
            'name': emotion.name
        }
    }

    return make_response(jsonify(data), 200)

@emotion_route.route('/emotion/<int:id>', methods=['DELETE'])
def delete_emotion(id):
    emotion = Emotion.query.get(id)
    db.session.delete(emotion)
    db.session.commit()
    data = {
        'message': 'Emotion deleted',
        'status': 200,
        'data': {}
    }

    return make_response(jsonify(data), 200)

