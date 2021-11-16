"""
Login controller class
"""
from flask import request, jsonify
from flask_restx import Resource, marshal
from ..service.login_service import handle_login_data
from ..dto.login_to import LoginDto
from ..dto.user_to import UserDto

api = LoginDto.api
_login_payload = LoginDto.login_payload
_user = UserDto.user

@api.route('')
class LoginEndpoint(Resource):
    
    # ***GET***
    @api.response(200, description="OK", model = _user)
    def get(self):
        """Get a list of all stats"""
        user = handle_login_data({"password": "123", "username": "multiKorzych"})
        return marshal(user, _user), 200
   