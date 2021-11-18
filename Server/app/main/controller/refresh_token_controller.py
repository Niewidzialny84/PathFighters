"""
Refresh token controller class
"""
from flask import request, jsonify
from flask_restx import Resource, marshal
from ..service.refresh_token_service import refresh_token
from ..dto.token_to import TokenDto

api = TokenDto.api
_token_payload = TokenDto.token_payload
_token_response = TokenDto.token_response
_token_response_payload = TokenDto.token_response_payload

@api.route('')
class RefreshTokenEndpoint(Resource):
    # ***POST***
    @api.response(200, description="OK", model = _token_response_payload)
    @api.response(400, description="BAD REQUEST", model = _token_response)
    @api.response(404, description="NOT FOUND", model = _token_response)
    @api.expect(_token_payload)
    def post(self):
        """Method using to refresh JWT token"""
        status_code, jwt_token = refresh_token(request.json)
        if status_code == 200:
            return marshal(jwt_token, _token_response_payload), 200
        elif status_code == 400:
            return marshal({"description":"BAD REQUEST"}, _token_response), status_code
        elif status_code == 404:
            return marshal({"description":"NOT FOUND"}, _token_response), status_code
 