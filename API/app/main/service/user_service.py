from logging import Logger
from app.main import db
from app.main.model.user_model import User
from app.main.schema.user_schema import users_schema, user_schema
from typing import Dict, Tuple
from flask import request, jsonify, make_response

def add_new_user(request):
    username = request['username']
    email = request['email']
    password = request['password']

    if (email and username and password) != None and User.query.filter_by(username = username).first() == None:
        user = User(username, email, password)
        db.session.add(user)
        db.session.commit()
        return 201
    elif User.query.filter_by(username = username).first() != None:
        return 409

def get_all_users():
    # users = list(User.query.all())
    # return make_response(jsonify(users_schema.dump(users)), 200)
    return  User.query.all()       

def get_user(username):
    user = User.query.filter_by(username = username).first()
    return user

def user_put(username, request):
        if not username:
            return make_response(jsonify({ 'Message': 'Must provide the proper username' }), 400)

        user = User.query.filter_by(username = username).first()

        if user == None:
            return make_response(jsonify({ 'Message': 'User not exist!' }), 404)

        username_new = request.json['username']
        email_new = request.json['email']
        password_new = request.json['password']
        user.password = password_new
        user.username = username_new
        user.email = email_new

        db.session.commit()
        return make_response(jsonify({'Message': f'User {user.username} altered.'}), 200)