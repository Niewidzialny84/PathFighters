from flask import request, jsonify, make_response
from flask_restx import Resource, marshal
from ..model.user_model import User
from ..util.dto import UserDto
from ..schema import user_schema
from ..service.user_service import add_new_user, get_user, get_all_users, user_put
from app.main import db

api = UserDto.api
_user = UserDto.user
_user_response = UserDto.user_response
_user_list = UserDto.user_list

@api.route('')
class UserList(Resource):
    
    # @staticmethod
    @api.doc('list_of_registered_users')
    # @api.marshal_list_with(_user, envelope='data')
    @api.response(200, description="OK", model = _user)
    @api.response(204, description="NO CONTENT", model = _user_response)
    def get(self):
        """get a lis of users"""
        users = get_all_users()
        
        if users == None:
            return marshal({'description':'NO CONTENT'}, _user_response), 204
        else:
            return marshal(users, _user), 200
       
    # @staticmethod
    @api.response(201, description="Created.", model = _user_response)
    def post(self):
        status_code = add_new_user(request.json)
        if status_code == 201:
            return marshal({'description':'Not found.'}, _user_response), 404
            
    # @staticmethod
    def put():
        try: username = request.args['username']
        except Exception as _: username = None
        user_put(username)

    # @staticmethod
    @api.response(200, description="OK.", model = _user_response)
    @api.response(400, description="Bad request.", model = _user_response)
    def patch(self):
        try: 
            username = request.args['username']
        except Exception as _: 
            username = None
            
        try:
            username_new = request.json['username']
        except Exception as _:
            username_new = None

        try:
            password_new = request.json['password']
        except Exception as _:
            password_new = None
        
        try:
            email_new = request.json['email']
        except Exception as _:
            email_new = None

        if username == None:
            return make_response(jsonify({ 'Message': 'Must provide the proper username' }), 400)

        user = User.query.filter_by(username = username).first()

        if user == None:
            return make_response(jsonify({ 'Message': 'User not exist!' }), 404)

        if username_new != None:
            user.username = username_new

        if password_new != None:
            user.password = password_new 
        
        if email_new != None:
            user.email = email_new

        db.session.commit()
        return make_response(jsonify({'Message': f'User {user.username} altered.'}), 200)

    # @staticmethod
    def delete():
        try: username = request.args['username']
        except Exception as _: username = None

        if not username:
            return make_response(jsonify({ 'Message': 'Must provide the user username' }), 400)

        user = User.query.filter_by(username = username).first()

        if user == None:
            return make_response(jsonify({ 'Message': 'User not exist!' }), 404)

        db.session.delete(user)
        db.session.commit()

        return make_response(jsonify({'Message': f'User {username} deleted.'}), 200)

@api.route('/<username>')
@api.param('username', 'The username identifier')
class User(Resource):
   
    @api.doc('user_with_specific_username')
    @api.response(200, description="OK", model = _user)
    @api.response(404, description="NOT FOUND", model = _user_response)
    def get(self, username):
        """get a user given its identifier"""
        user = get_user(username)
    
        if not user:
            return marshal({'description':'NOT FOUND'}, _user_response), 404
        else:
            return marshal(user, _user), 200
       
