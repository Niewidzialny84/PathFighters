from flask import request
from flask_restx import Resource, marshal
from ..util.user_to import UserDto
from ..service.user_service import delete_user, get_all_users, add_new_user, delete_all_users, get_user, user_patch, user_patch_by_id, user_put, user_put_by_id, get_user_by_id, delete_user, delete_user_by_id

api = UserDto.api
_user = UserDto.user
_user_response = UserDto.user_response
_user_payload = UserDto.user_payload
_user_payload_patch = UserDto.user_payload_patch

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
        
        if users == []:
            return marshal({'description':'NO CONTENT'}, _user_response), 204
        else:
            return marshal(users, _user), 200
    
    # ***POST***
    @api.doc('post_new_user')
    @api.response(201, description="CREATED", model = _user_response)
    @api.response(409, description="CONFLICT", model = _user_response)
    @api.expect(_user_payload)
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
        
        return marshal(user, _user), 200
    
    # ***PUT***
    @api.doc('put_user_with_specific_username')
    @api.response(200, description="OK", model = _user_response)
    @api.response(400, description="BAD REQUEST", model = _user_response)
    @api.response(404, description="NOT FOUND", model = _user_response)
    @api.expect(_user_payload)
    def put(self, username):
        """Put a user with given identifier"""
        status_code = user_put(username, request.json)
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
    @api.expect(_user_payload_patch, validate=False)
    def patch(self, username):
        """Patch a user with given identifier"""
        status_code = user_patch(username, request.json)
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

@api.route('/id/<userid>')
@api.param('userid', 'The user identifier')
class UserById(Resource):
   
    # ***GET***
    @api.doc('return_user_with_specific_is.')
    @api.response(200, description="OK", model = _user)
    @api.response(404, description="NOT FOUND", model = _user_response)
    def get(self, userid):
        """Get a user with given identifier"""
        user = get_user_by_id(userid)
        if not user:
            return marshal({'description':'NOT FOUND'}, _user_response), 404
        else:
            return marshal(user, _user), 200
    
    # ***DELETE***
    @api.doc('delete_user_with_specific_id')
    @api.response(200, description="OK", model = _user_response)
    @api.response(404, description="NOT FOUND", model = _user_response)
    def delete(self, userid):
        """Delete a user with given identifier"""
        status_code = delete_user_by_id(userid)
        if status_code == 200:
            return marshal({'description':'OK'}, _user_response), 200
        elif status_code == 404:
            return marshal({'description':'NOT FOUND'}, _user_response), 404
    
    # ***PUT***
    @api.doc('put_user_with_specific_id')
    @api.response(200, description="OK", model = _user_response)
    @api.response(400, description="BAD REQUEST", model = _user_response)
    @api.response(404, description="NOT FOUND", model = _user_response)
    @api.expect(_user_payload)
    def put(self, userid):
        """Put a user with given identifier"""
        status_code = user_put_by_id(userid, request.json)
        if status_code == 200:
            return marshal({'description':'OK'}, _user_response), 200
        elif status_code == 400:
            return marshal({'description':'BAD REQUEST'}, _user_response), 400
        elif status_code == 404:
            return marshal({'description':'NOT FOUND'}, _user_response), 404
    
    # ***PATCH***
    @api.doc('patch_user_with_specific_id')
    @api.response(200, description="OK", model = _user_response)
    @api.response(400, description="BAD REQUEST", model = _user_response)
    @api.response(404, description="NOT FOUND", model = _user_response)
    @api.expect(_user_payload_patch, validate=False)
    def patch(self, userid):
        """Patch a user with given identifier"""
        status_code = user_patch_by_id(userid, request.json)
        if status_code == 200:
            return marshal({'description':'OK'}, _user_response), 200
        elif status_code == 400:
            return marshal({'description':'BAD REQUEST'}, _user_response), 400
        elif status_code == 404:
            return marshal({'description':'NOT FOUND'}, _user_response), 404