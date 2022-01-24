from flask_restx import Namespace, fields
from app.main.dto.user_to import UserDto

class LoginDto:
    api = Namespace('login', description='login related data')

    login_payload = api.model('login_payload', {
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password')
    })

    login_successful = api.model('login_successful',{
        'user': fields.Nested(UserDto.user),
        'jwt_token': fields.String(required=True, description='JSON web token'),
    })
    