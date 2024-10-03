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
    return make_response(jsonify({'message': 'Emotion created'}), 200)

@emotion_route.route('/emotions', methods=['GET'])
def get_emotions():
    emotions = Emotion.query.all()
    return jsonify([emotion.serialize() for emotion in emotions])

@emotion_route.route('/emotion/<int:id>', methods=['GET'])
def get_emotion(id):
    emotion = Emotion.query.get(id)
    return jsonify(emotion.serialize())

@emotion_route.route('/emotion/<int:id>', methods=['PUT'])
def update_emotion(id):
    emotion = Emotion.query.get(id)
    emotion.name = request.json['name']
    db.session.commit()
    return make_response(jsonify({'message': 'Emotion updated'}), 200)

@emotion_route.route('/emotion/<int:id>', methods=['DELETE'])
def delete_emotion(id):
    emotion = Emotion.query.get(id)
    db.session.delete(emotion)
    db.session.commit()
    return make_response(jsonify({'message': 'Emotion deleted'}), 200)