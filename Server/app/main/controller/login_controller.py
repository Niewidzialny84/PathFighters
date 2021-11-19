"""
Login controller class
"""
from flask import request
from flask_restx import Resource, marshal
from ..service.login_service import handle_login_data
from ..dto.login_to import LoginDto
from ..dto.user_to import UserDto

api = LoginDto.api
_login_payload = LoginDto.login_payload
_user_response = UserDto.user_response
_login_successful = LoginDto.login_successful

@api.route('')
class LoginEndpoint(Resource):
    # ***POST***
    @api.response(200, description="OK", model = _login_successful)
    @api.response(400, description="BAD REQUEST", model = _user_response)
    @api.response(404, description="NOT FOUND", model = _user_response)
    @api.expect(_login_payload)
    def post(self):
        """Method using to login user"""
        status_code, authenticated_user = handle_login_data(request.json)

        if status_code == 200:
            return marshal(authenticated_user, _login_successful), status_code
        elif status_code == 400:
            return marshal({"description":"BAD REQUEST"}, _user_response), status_code
        elif status_code == 404:
            return marshal({"description":"NOT FOUND"}, _user_response), status_code
 