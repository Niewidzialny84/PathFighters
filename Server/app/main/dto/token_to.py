from flask_restx import Namespace, fields

class TokenDto:
    api = Namespace('login', description='login related data')

    token_response = api.model('token_response',{
        'description': fields.String(required=True),
    })

    token_response_payload = api.model('token_response_payload',{
        'jwt_token': fields.String(required=True),
    })

    token_payload = api.model('login_payload', {
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password')
    })