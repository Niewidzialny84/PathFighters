from flask_restx import Namespace, fields

class RegisterDto:
    api = Namespace('register', description='user related operations')

    register_response = api.model('register_response',{
        'description': fields.String(required=True),
    })