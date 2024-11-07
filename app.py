from flask import Flask
from flask_cors import CORS
from utils.db import db
from config import DATABASE_CONNECTION
from services.emotion_detection_route import emotion_detection_route
from services.login_route import login_route
from services.emotion_route import emotion_route
from services.register_route import register_route
from services.gender_route import gender_route
from services.ubigeo_route import ubigeo_route
from services.document_type_route import document_type_route
from services.role_route import role_route

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Registrar los blueprints correctamente
app.register_blueprint(emotion_detection_route)
app.register_blueprint(login_route)
app.register_blueprint(emotion_route)
app.register_blueprint(register_route)
app.register_blueprint(gender_route)
app.register_blueprint(ubigeo_route)
app.register_blueprint(document_type_route)
app.register_blueprint(role_route)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)