from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.emotion_detection import Emotion_detection
from model.emotion import Emotion
from model.users import Users

emotion_detection_route = Blueprint('emotion_detection_route', __name__)

@emotion_detection_route.route('/emotion_detection', methods=['POST'])
def create_emotion_detection():
    id_user = request.json['id_user']
    emotion = request.json['emotion']
    confidence = request.json['confidence']
    
    id_emotion = Emotion.query.filter_by(name=emotion).first().id

    emotion_detection = Emotion_detection(id_user, id_emotion, confidence)
    db.session.add(emotion_detection)
    db.session.commit()
    return make_response(jsonify({'message': 'Emotion detection created'}), 200)

@emotion_detection_route.route('/emotion_detections', methods=['GET'])
def get_emotion_detections():
    emotion_detections = Emotion_detection.query.all()
    data = {
        'message': 'Emotion detections fetched',
        'status': 200,
        'data': []
    }

    for emotion_detection in emotion_detections:
        data['data'].append({
            'id_user': emotion_detection.id_user,
            'id_emotion': emotion_detection.id_emotion,
            'detection_time': emotion_detection.detection_time,
            'confidence': emotion_detection.confidence
        })

    return make_response(jsonify(data), 200)

@emotion_detection_route.route('/emotion_detection/<int:id_user>', methods=['GET'])
def get_emotion_detection(id_user):
    emotion_detection = Emotion_detection.query.filter_by(id_user=id_user).all()
    data = {
        'message': 'Emotion detection fetched',
        'status': 200,
        'data': []
    }

    for emotion in emotion_detection:
        data['data'].append({
            'id_user': emotion.id_user,
            'id_emotion': emotion.id_emotion,
            'detection_time': emotion.detection_time,
            'confidence': emotion.confidence
        })

    return make_response(jsonify(data), 200)
