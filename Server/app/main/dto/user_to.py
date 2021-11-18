from flask_restx import Namespace, fields

class UserDto:
    api = Namespace('user', description='user related operations')

    user = api.model('user', {
        'id': fields.Integer(description='user Identifier'),
        'username': fields.String(required=True, description='user username'),
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password')
    })

    user_list = api.model('user_list', {
        'users': fields.List(fields.Nested(user)),
    })

    user_response = api.model('user_response',{
        'description': fields.String(required=True),
    })

    user_payload = api.model('user_payload', {
        'username': fields.String(required=True, description='user username'),
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password')
    })

    user_payload_patch = api.model('user_payload_patch', {
        'username': fields.String(required=False, description='user username'),
        'email': fields.String(required=False, description='user email address'),
        'password': fields.String(required=False, description='user password')
    })