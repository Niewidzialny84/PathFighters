"""
Login controller class
"""
from flask import request, jsonify
from flask_restx import Resource, marshal
from requests.sessions import Request
from ..service.logout_service import handle_logout
from ..dto.logout_to import LogoutDto

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import get_jwt
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import unset_jwt_cookies

api = LogoutDto.api
_logout_response = LogoutDto.logout_response

@api.route('')
class LogoutEndpoint(Resource):
    # ***POST***
    @api.response(200, description="OK", model = _logout_response)
    @jwt_required()
    def delete(self):
        """Method using to logout user"""
        handle_logout()
        return marshal({"description":"OK"}, _logout_response), 200