"""
User service file.
"""
from app.main import db # pragma: no cover 
from app.main.model.user_model import User # pragma: no cover 
from app.main.service.stats_service import create_new_stats, delete_all_stats, delete_stats # pragma: no cover 
 
def add_new_user(request_json):
    username = request_json['username']
    email = request_json['email']
    password = request_json['password']

    if (email and username and password) != None and User.query.filter_by(username = username).first() == None:
        user = User(username, email, password)
        db.session.add(user)
        db.session.commit()
        userid = User.query.filter_by(username = username).first().id
        create_new_stats(userid)
        return 201
    elif User.query.filter_by(username = username).first() != None:
        return 409

def get_all_users():
    return  User.query.all()       

def get_user(username):
    user = User.query.filter_by(username = username).first()
    return user

def get_user_by_id(userid):
    user = User.query.filter_by(id = userid).first()
    return user

def user_put(username, request_json):
    user = User.query.filter_by(username = username).first()

    if user is None:
        return 404

    try:
        username_new = request_json['username']
    except Exception as _:
        username_new = None

    try:
        password_new = request_json['password']
    except Exception as _:
        password_new = None
    
    try:
        email_new = request_json['email']
    except Exception as _:
        email_new = None

    if None in [username_new, email_new, password_new]:
        return 400

    user.password = password_new
    user.username = username_new
    user.email = email_new

    db.session.commit()
    return 200

def user_put_by_id(id, request_json):
    user = User.query.filter_by(id = id).first()

    if user is None:
        return 404

    try:
        username_new = request_json['username']
    except Exception as _:
        username_new = None

    try:
        password_new = request_json['password']
    except Exception as _:
        password_new = None
    
    try:
        email_new = request_json['email']
    except Exception as _:
        email_new = None

    if None in [username_new, email_new, password_new]:
        return 400

    user.password = password_new
    user.username = username_new
    user.email = email_new

    db.session.commit()
    return 200

def delete_all_users():
    delete_all_stats()
    db.session.query(User).delete()
    db.session.commit()

def delete_user(username):
    user = User.query.filter_by(username = username).first()

    if user is None:
        return 404

    delete_stats(user.id)
    db.session.delete(user)
    db.session.commit()
    return 200

def delete_user_by_id(userid):
    user = User.query.filter_by(id = userid).first()

    if user is None:
        return 404

    delete_stats(user.id)
    db.session.delete(user)
    db.session.commit()
    return 200

def user_patch(username, request_json):
    try:
        username_new = request_json['username']
    except Exception as _:
        username_new = None

    try:
        password_new = request_json['password']
    except Exception as _:
        password_new = None
    
    try:
        email_new = request_json['email']
    except Exception as _:
        email_new = None

    if username == None:
        return 400

    user = User.query.filter_by(username = username).first()

    if user == None:
        return 404

    if username_new is not None:
        user.username = username_new

    if password_new is not None:
        user.password = password_new
    
    if email_new is not None:
        user.email = email_new

    db.session.commit()
    return 200

def user_patch_by_id(id, request_json):  
    try:
        username_new = request_json['username']
    except Exception as _:
        username_new = None

    try:
        password_new = request_json['password']
    except Exception as _:
        password_new = None
    
    try:
        email_new = request_json['email']
    except Exception as _:
        email_new = None

    if id == None:
        return 400

    user = User.query.filter_by(id = id).first()

    if user is None:
        return 404

    if username_new is not None:
        user.username = username_new

    if password_new is not None:
        user.password = password_new
    
    if email_new is not None:
        user.email = email_new

    db.session.commit()
    return 200