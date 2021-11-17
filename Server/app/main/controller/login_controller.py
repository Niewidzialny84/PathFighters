"""
Login controller class
"""
from flask import request, jsonify
from flask_restx import Resource, marshal
from requests.sessions import Request
from ..service.login_service import handle_login_data
from ..dto.login_to import LoginDto
from ..dto.user_to import UserDto

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import get_jwt
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import unset_jwt_cookies

api = LoginDto.api
_login_payload = LoginDto.login_payload
_user_response = UserDto.user_response
_login_succesful = LoginDto.login_succesful

@api.route('')
class LoginEndpoint(Resource):
    
    # ***POST***
    @api.response(200, description="OK", model = _login_succesful)
    @api.response(400, description="BAD REQUEST", model = _user_response)
    @api.response(404, description="NOT FOUND", model = _user_response)
    @api.expect(_login_payload)
    def post(self):
        """Method using to login user"""
        status_code, authenticated_user = handle_login_data(request.json)

        # user_JSON = jsonpickle.encode(user, unpicklable=False)
        # return jsonpickle.decode(user_JSON)

        if status_code == 200:
            return marshal(authenticated_user, _login_succesful), status_code
        elif status_code == 400:
            return marshal({"description":"BAD REQUEST"}, _user_response), status_code
        elif status_code == 404:
            return marshal({"description":"NOT FOUND"}, _user_response), status_code
    
    # @jwt_required()
    # def get(self):       
    #     current_user = get_jwt_identity()
    #     print(current_user)
    #     return "", 200

   