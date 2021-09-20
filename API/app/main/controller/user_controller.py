from flask import request, jsonify, make_response
from flask_restx import Resource, marshal
from ..model.user_model import User
from ..util.dto import UserDto
from ..schema import user_schema
from ..service.user_service import *
from app.main import db

api = UserDto.api
_user = UserDto.user
_user_response = UserDto.user_response
_user_list = UserDto.user_list

@api.route('')
class UserList(Resource):
    
    # ***GET***
    # @api.marshal_list_with(_user, envelope='data')
    @api.doc('list_of_registered_users')
    @api.response(200, description="OK", model = _user)
    @api.response(204, description="NO CONTENT", model = _user_response)
    def get(self):
        """Get a list of users"""
        users = get_all_users()
        
        if users == None:
            return marshal({'description':'NO CONTENT'}, _user_response), 204
        else:
            return marshal(users, _user), 200
    
    # ***POST***
    @api.doc('post_new_user')
    @api.response(201, description="CREATED", model = _user_response)
    @api.response(409, description="CONFLICT", model = _user_response)
    def post(self):
        """Create new user."""
        status_code = add_new_user(request.json)
        if status_code == 201:
            return marshal({'description':'CREATED'}, _user_response), 201
        elif status_code == 409:
            return marshal({'description':'CONFLICT'}, _user_response), 409

    # ***DELETE***
    @api.doc('delete_all_users')
    @api.response(200, description="OK", model = _user_response)
    def delete(self):
        """Delete all users."""
        delete_all_users()
        return marshal({'description':'OK'}, _user_response), 200

@api.route('/<username>')
@api.param('username', 'The username identifier')
class User(Resource):
   
    # ***GET***
    @api.doc('return_user_with_specific_username.')
    @api.response(200, description="OK", model = _user)
    @api.response(404, description="NOT FOUND", model = _user_response)
    def get(self, username):
        """Get a user with given identifier"""
        user = get_user(username)
        if not user:
            return marshal({'description':'NOT FOUND'}, _user_response), 404
        else:
            return marshal(user, _user), 200
    
    # ***PUT***
    @api.doc('put_user_with_specific_username')
    @api.response(200, description="OK", model = _user_response)
    @api.response(400, description="BAD REQUEST", model = _user_response)
    @api.response(404, description="NOT FOUND", model = _user_response)
    def put(self, username):
        """Put a user with given identifier"""
        status_code = user_put(username)
        if status_code == 200:
            return marshal({'description':'OK'}, _user_response), 200
        elif status_code == 400:
            return marshal({'description':'BAD REQUEST'}, _user_response), 400
        elif status_code == 404:
            return marshal({'description':'NOT FOUND'}, _user_response), 404

    # ***PATCH***
    @api.doc('patch_user_with_specific_username')
    @api.response(200, description="OK", model = _user_response)
    @api.response(400, description="BAD REQUEST", model = _user_response)
    @api.response(404, description="NOT FOUND", model = _user_response)
    def patch(self, username):
        """Patch a user with given identifier"""
        status_code = user_patch(username, request)
        if status_code == 200:
            return marshal({'description':'OK'}, _user_response), 200
        elif status_code == 400:
            return marshal({'description':'BAD REQUEST'}, _user_response), 400
        elif status_code == 404:
            return marshal({'description':'NOT FOUND'}, _user_response), 404

    # ***DELETE***
    @api.doc('delete_user_with_specific_username')
    @api.response(200, description="OK", model = _user_response)
    @api.response(404, description="NOT FOUND", model = _user_response)
    def delete(self, username):
        """Delete a user with given identifier"""
        status_code = delete_user(username)
        if status_code == 200:
            return marshal({'description':'OK'}, _user_response), 200
        elif status_code == 404:
            return marshal({'description':'NOT FOUND'}, _user_response), 404