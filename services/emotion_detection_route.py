from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.emotion_detection import Emotion_detection

emotion_detection_route = Blueprint('emotion_detection_route', __name__)

@emotion_detection_route.route('/emotion_detection', methods=['POST'])
def create_emotion_detection():
    id_user = request.json['id_user']
    emotion = request.json['emotion']
    id_emotion = emotion['id']
    confidence = request.json['confidence']
    emotion_detection = Emotion_detection(id_user, id_emotion, confidence)
    db.session.add(emotion_detection)
    db.session.commit()
    return make_response(jsonify({'message': 'Emotion detection created'}), 200)

@emotion_detection_route.route('/emotion_detections', methods=['GET'])
def get_emotion_detections():
    emotion_detections = Emotion_detection.query.all()
    return jsonify([emotion_detection.serialize() for emotion_detection in emotion_detections])