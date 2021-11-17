from flask import request
from flask_restx import Resource, marshal
from ..dto.user_to import UserDto
from ..service.users_service import *
from flask_jwt_extended import jwt_required

api = UserDto.api
_user = UserDto.user
_user_response = UserDto.user_response
_user_payload_patch = UserDto.user_payload_patch

@api.route('')
class UserList(Resource):
    # ***GET***
    @api.doc('list_of_registered_users')
    @api.response(200, description="OK", model = _user)
    @api.response(204, description="NO CONTENT", model = _user_response)
    @jwt_required()
    def get(self):
        """Get a list of users"""
        status_code, users = api_get_users()
        
        if users == None:
            return marshal({'description':'NO CONTENT'}, _user_response), 204
        else:
            return marshal(users, _user), 200

@api.route('/id/<userid>')
@api.param('userid', 'The user identifier')
class UserById(Resource):
    # ***GET***
    @api.doc('return_user_with_specific_id')
    @api.response(200, description="OK", model = _user)
    @api.response(404, description="NOT FOUND", model = _user_response)
    @jwt_required()
    def get(self, userid):
        """Get a user with given identifier"""
        status_code, user = api_get_user_by_id(userid)
        if not user:
            return marshal({'description':'NOT FOUND'}, _user_response), 404
        else:
            return marshal(user, _user), 200
    
    # ***DELETE***
    @api.doc('delete_user_with_specific_id')
    @api.response(200, description="OK", model = _user_response)
    @api.response(404, description="NOT FOUND", model = _user_response)
    @jwt_required()
    def delete(self, userid):
        """Delete a user with given identifier"""
        status_code = api_delete_user_by_id(userid)
        if status_code == 200:
            return marshal({'description':'OK'}, _user_response), 200
        elif status_code == 404:
            return marshal({'description':'NOT FOUND'}, _user_response), 404
    
    # ***PATCH***
    @api.doc('patch_user_with_specific_id')
    @api.response(200, description="OK", model = _user_response)
    @api.response(400, description="BAD REQUEST", model = _user_response)
    @api.response(404, description="NOT FOUND", model = _user_response)
    @api.expect(_user_payload_patch, validate=False)
    @jwt_required()
    def patch(self, userid):
        """Patch a user with given identifier"""
        status_code = api_update_user_by_id(userid, request.json)
        if status_code == 200:
            return marshal({'description':'OK'}, _user_response), 200
        elif status_code == 400:
            return marshal({'description':'BAD REQUEST'}, _user_response), 400
        elif status_code == 404:
            return marshal({'description':'NOT FOUND'}, _user_response), 404