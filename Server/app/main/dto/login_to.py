from flask_restx import Namespace, fields
from app.main.dto.user_to import UserDto

class LoginDto:
    api = Namespace('login', description='login related data')

    login_payload = api.model('login', {
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password')
    })

    login_response = api.model('login_response',{
        'description': fields.String(required=True),
    })

    token_payload = api.model('login_succesful',{
        'jwt': fields.String(required=True),
    })

    login_succesful = api.model('login_succesful',{
        'user': fields.Nested(UserDto.user),
        'token': fields.String(required=True, description='JSON web token'),
    })