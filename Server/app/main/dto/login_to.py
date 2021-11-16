from flask_restx import Namespace, fields

class LoginDto:
    api = Namespace('login', description='login related data')

    login_payload = api.model('login', {
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password')
    })

    login_response = api.model('login_response',{
        'description': fields.String(required=True),
    })