"""
Stats service file.
"""
from app.main import db # pragma: no cover
from app.main.model.stats_model import Stats # pragma: no cover

def create_new_stats(userid):
    total = 0
    fails = 0
    wins = 0
    stats = Stats(userid, total, fails, wins)
    db.session.add(stats)
    db.session.commit()

def get_all_stats():
    return  Stats.query.all()       

def get_user_stats(userid):
    stats = Stats.query.filter_by(userid = userid).first()
    return stats

def stats_put(userid, request_json):
    try:
        total_new = request_json['total']
    except Exception as _:
        total_new = None

    try:
        wins_new = request_json['wins']
    except Exception as _:
        wins_new = None
    
    try:
        fails_new = request_json['fails']
    except Exception as _:
        fails_new = None

    if None in [userid, total_new, wins_new, fails_new]:
        return 400
    
    stats = Stats.query.filter_by(userid = userid).first()

    if stats is None:
        return 404

    stats.total = total_new
    stats.wins = wins_new
    stats.fails = fails_new

    db.session.commit()
    return 200

def delete_all_stats():
    db.session.query(Stats).delete()
    db.session.commit()

def delete_stats(userid):
    stats = Stats.query.filter_by(userid = userid).first()

    if stats == None:
        return 404

    db.session.delete(stats)
    db.session.commit()
    return 200

def stats_patch(userid, request_json):
    try:
        total_new = request_json['total']
    except Exception as _:
        total_new = None

    try:
        wins_new = request_json['wins']
    except Exception as _:
        wins_new = None
    
    try:
        fails_new = request_json['fails']
    except Exception as _:
        fails_new = None

    if userid is None:
        return 400

    stats = Stats.query.filter_by(userid = userid).first()

    if stats is None:
        return 404

    if total_new is not None:
        stats.total = total_new

    if wins_new is not None:
        stats.wins = wins_new
    
    if fails_new is not None:
        stats.fails = fails_new

    db.session.commit()
    return 200        

def stats_add_win(userid):
    if userid is None:
        return 400

    stats = Stats.query.filter_by(userid = userid).first()

    if stats is None:
        return 404

    total_old = stats.total
    wins_old = stats.wins
    
    stats.total = total_old + 1
    stats.wins = wins_old + 1

    db.session.commit()
    return 200        

def stats_add_fail(userid):
    if userid is None:
        return 400

    stats = Stats.query.filter_by(userid = userid).first()

    if stats is None:
        return 404

    total_old = stats.total
    fails_old = stats.fails
    
    stats.total = total_old + 1
    stats.fails = fails_old + 1

    db.session.commit()
    return 200  