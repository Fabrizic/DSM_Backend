from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.document_type import DocumentType

document_type_route = Blueprint('document_type_route', __name__)

@document_type_route.route('/document_type', methods=['GET'])
def get_document_types():
    document_types = DocumentType.query.all()
    data = {
        'message': 'Todos los tipos de documentos',
        'status': 200,
        'data': [
            {
                'id': document_type.id,
                'document_type': document_type.type,
                'length': document_type.length
            } for document_type in document_types
        ]
    }

    return make_response(jsonify(data), 200)