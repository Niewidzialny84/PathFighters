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
    return  User.query.all()       

def get_user(username):
    user = User.query.filter_by(username = username).first()
    return user

def user_put(username, request):
    user = User.query.filter_by(username = username).first()

    if user == None:
        return 404

    username_new = request.json['username']
    email_new = request.json['email']
    password_new = request.json['password']

    if (username_new or email_new or password_new) == None:
        return 400

    user.password = password_new
    user.username = username_new
    user.email = email_new

    db.session.commit()
    return 200

def delete_all_users():
    User.query.delete(users_schema).delete()
    db.session.commit()

def delete_user(username):
    user = User.query.filter_by(username = username).first()

    if user == None:
        return 404

    db.session.delete(user)
    db.session.commit()
    return 200

def user_patch(username, request):  
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
        return 400

    user = User.query.filter_by(username = username).first()

    if user == None:
        return 404

    if username_new != None:
        user.username = username_new

    if password_new != None:
        user.password = password_new 
    
    if email_new != None:
        user.email = email_new

    db.session.commit()
    return 200