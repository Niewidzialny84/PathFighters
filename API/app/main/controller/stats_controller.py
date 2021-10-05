from flask import request, jsonify, make_response
from flask_restx import Resource, marshal
from ..model.stats_model import Stats
from ..util.stats_to import StatsDto
from ..schema import stats_schema
from ..service.stats_service import *
from app.main import db

api = StatsDto.api
_stats = StatsDto.stats
_stats_response = StatsDto.stats_response
_stats_payload = StatsDto.stats_payload
_stats_payload_patch = StatsDto.stats_payload_patch

@api.route('')
class StatsList(Resource):
    
    # ***GET***
    # @api.marshal_list_with(_stats, envelope='data')
    @api.doc('list_of_all_stats')
    @api.response(200, description="OK", model = _stats)
    @api.response(204, description="NO CONTENT", model = _stats_response)
    def get(self):
        """Get a list of all stats"""
        stats = get_all_stats()
        
        if stats == None:
            return marshal({'description':'NO CONTENT'}, _stats_response), 204
        else:
            return marshal(stats, _stats), 200

@api.route('/<userid>')
@api.param('userid', 'The userid identifier')
class Stats(Resource):
   
    # ***GET***
    @api.doc('return_stats_for_user_with_specific_username.')
    @api.response(200, description="OK", model = _stats)
    @api.response(404, description="NOT FOUND", model = _stats_response)
    def get(self, userid):
        """Get a user with given identifier"""
        stats = get_user_stats(userid)
        if not stats:
            return marshal({'description':'NOT FOUND'}, _stats_response), 404
        else:
            return marshal(stats, _stats), 200
    
    # ***PUT***
    @api.doc('put_stats_for_user_with_specific_userid')
    @api.response(200, description="OK", model = _stats_response)
    @api.response(400, description="BAD REQUEST", model = _stats_response)
    @api.response(404, description="NOT FOUND", model = _stats_response)
    @api.expect(_stats_payload)
    def put(self, userid):
        """Put a stats for user with given identifier"""
        status_code = stats_put(userid, request.json)
        if status_code == 200:
            return marshal({'description':'OK'}, _stats_response), 200
        elif status_code == 400:
            return marshal({'description':'BAD REQUEST'}, _stats_response), 400
        elif status_code == 404:
            return marshal({'description':'NOT FOUND'}, _stats_response), 404

    # ***PATCH***
    @api.doc('patch_stats_for_user_with_specific_username')
    @api.response(200, description="OK", model = _stats_response)
    @api.response(400, description="BAD REQUEST", model = _stats_response)
    @api.response(404, description="NOT FOUND", model = _stats_response)
    @api.expect(_stats_payload_patch, validate=False)
    def patch(self, userid):
        """Patch a stats for user with given identifier"""
        status_code = stats_patch(userid, request.json)
        if status_code == 200:
            return marshal({'description':'OK'}, _stats_response), 200
        elif status_code == 400:
            return marshal({'description':'BAD REQUEST'}, _stats_response), 400
        elif status_code == 404:
            return marshal({'description':'NOT FOUND'}, _stats_response), 404

@api.route('/<userid>/add-win')
@api.param('userid', 'The user identifier')
class Stats_wins(Resource):
   
    # ***PATCH***
    @api.doc('add_win_and_total_to_stats_for_user_with_given_username')
    @api.response(200, description="OK", model = _stats_response)
    @api.response(400, description="BAD REQUEST", model = _stats_response)
    @api.response(404, description="NOT FOUND", model = _stats_response)
    def patch(self, userid):
        """Patch a wins for user with given identifier"""
        status_code = stats_add_win(userid)
        if status_code == 200:
            return marshal({'description':'OK'}, _stats_response), 200
        elif status_code == 400:
            return marshal({'description':'BAD REQUEST'}, _stats_response), 400
        elif status_code == 404:
            return marshal({'description':'NOT FOUND'}, _stats_response), 404

@api.route('/<userid>/add-fail')
@api.param('userid', 'The user identifier')
class Stats_fails(Resource):
   
    # ***PATCH***
    @api.doc('add_fails_and_total_to_stats_for_user_with_given_username')
    @api.response(200, description="OK", model = _stats_response)
    @api.response(400, description="BAD REQUEST", model = _stats_response)
    @api.response(404, description="NOT FOUND", model = _stats_response)
    def patch(self, userid):
        """Patch a fails for user with given identifier"""
        status_code = stats_add_fails(userid)
        if status_code == 200:
            return marshal({'description':'OK'}, _stats_response), 200
        elif status_code == 400:
            return marshal({'description':'BAD REQUEST'}, _stats_response), 400
        elif status_code == 404:
            return marshal({'description':'NOT FOUND'}, _stats_response), 404