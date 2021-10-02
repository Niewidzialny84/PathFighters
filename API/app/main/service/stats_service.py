from logging import Logger
from app.main import db
from app.main.model.stats_model import Stats
from app.main.schema.stats_schema import stats_schema, stat_schema
from typing import Dict, Tuple
from flask import request, jsonify, make_response

def create_new_stats(username):
    total = 0
    fails = 0
    wins = 0
    stats = Stats(username, total, fails, wins)
    db.session.add(stats)
    db.session.commit()

def get_all_stats():
    return  Stats.query.all()       

def get_user_stats(username):
    stats = Stats.query.filter_by(username = username).first()
    return stats

def stats_put(username, request):
    stats = Stats.query.filter_by(username = username).first()

    if stats == None:
        return 404

    total_new = request.json['total']
    wins_new = request.json['wins']
    fails_new = request.json['fails']

    if (total_new or wins_new or fails_new) == None:
        return 400

    stats.total = total_new
    stats.wins = wins_new
    stats.fails = fails_new

    db.session.commit()
    return 200

def delete_all_stats():
    db.session.query(Stats).delete()
    db.session.commit()

def delete_stats(username):
    stats = Stats.query.filter_by(username = username).first()

    if stats == None:
        return 404

    db.session.delete(stats)
    db.session.commit()
    return 200

def stats_patch(username, request):
    try:
        username_new = request.json['username']
    except Exception as _:
        username_new = None

    try:
        total_new = request.json['total']
    except Exception as _:
        total_new = None

    try:
        wins_new = request.json['wins']
    except Exception as _:
        wins_new = None
    
    try:
        fails_new = request.json['fails']
    except Exception as _:
        fails_new = None

    if username == None:
        return 400

    stats = Stats.query.filter_by(username = username).first()

    if stats == None:
        return 404

    if username_new != None:
        stats.username = username_new

    if total_new != None:
        stats.total = total_new

    if wins_new != None:
        stats.wins = wins_new 
    
    if fails_new != None:
        stats.fails = fails_new

    db.session.commit()
    return 200        

def stats_add_win(username):
    if username == None:
        return 400

    stats = Stats.query.filter_by(username = username).first()

    if stats == None:
        return 404

    total_old = stats.total
    wins_old = stats.wins
    
    stats.total = total_old + 1
    stats.wins = wins_old + 1

    db.session.commit()
    return 200        

def stats_add_fails(username):
    if username == None:
        return 400

    stats = Stats.query.filter_by(username = username).first()

    if stats == None:
        return 404

    total_old = stats.total
    fails_old = stats.fails
    
    stats.total = total_old + 1
    stats.fails = fails_old + 1

    db.session.commit()
    return 200  