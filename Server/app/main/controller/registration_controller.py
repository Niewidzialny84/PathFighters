"""
Registration controller class
"""
from flask import request
from flask_restx import Resource, marshal
from ..dto.user_to import UserDto
from ..dto.register_to import RegisterDto
from ..service.registration_service import api_add_user

api = RegisterDto.api
_register_response = RegisterDto.register_response
_user_payload = UserDto.user_payload

@api.route('')
class Register(Resource):
    # ***POST***
    @api.doc('post_new_user')
    @api.response(201, description="CREATED", model = _register_response)
    @api.response(409, description="CONFLICT", model = _register_response)
    @api.expect(_user_payload)
    def post(self):
        """Handle registration process and if True create new user."""
        status_code = api_add_user(request.json)
        if status_code == 201:
            return marshal({'description':'CREATED'}, _register_response), 201
        elif status_code == 409:
            return marshal({'description':'CONFLICT'}, _register_response), 409
