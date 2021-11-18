from flask_restx import Namespace, fields

class LogoutDto:
    api = Namespace('login', description='login related data')

    logout_response = api.model('logout_response',{
        'description': fields.String(required=True),
    })