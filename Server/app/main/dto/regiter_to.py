from flask_restx import Namespace, fields

class RegisterDto:
    api = Namespace('register', description='user related operations')

    register_response = api.model('user_response',{
        'description': fields.String(required=True),
    })