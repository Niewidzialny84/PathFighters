from flask_restx import Namespace, fields

class StatsDto:
    api = Namespace('stats', description='stats related operations')
    
    stats = api.model('stats', {
        'id': fields.Integer(description='stats Identifier'),
        'userid': fields.Integer(required=True, description='user id'),
        'total': fields.Integer(required=True, description='total user games'),
        'fails': fields.Integer(required=True, description='total user fails'),
        'wins': fields.Integer(required=True, description='total user wins')
    })

    stats_list = api.model('stats_list', {
        'stats': fields.List(fields.Nested(stats)),
    })

    stats_response = api.model('stats_response',{
        'description': fields.String(required=True),
    })

    stats_payload = api.model('stats_payload',{
        'total': fields.Integer(required=True, description='total user games'),
        'fails': fields.Integer(required=True, description='total user fails'),
        'wins': fields.Integer(required=True, description='total user wins')
    })

    stats_payload_patch = api.model('stats_payload',{
        'total': fields.Integer(required=False, description='total user games'),
        'fails': fields.Integer(required=False, description='total user fails'),
        'wins': fields.Integer(required=False, description='total user wins')
    })
    