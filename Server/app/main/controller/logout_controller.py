"""
Logout controller class
"""
from flask_restx import Resource, marshal
from ..service.logout_service import handle_logout
from ..dto.logout_to import LogoutDto
from flask_jwt_extended import jwt_required

api = LogoutDto.api
_logout_response = LogoutDto.logout_response

@api.route('')
class LogoutEndpoint(Resource):
    # ***DELETE***
    @api.response(200, description="OK", model = _logout_response)
    @jwt_required()
    def delete(self):
        """Method using to logout user"""
        handle_logout()
        return marshal({"description":"OK"}, _logout_response), 200
