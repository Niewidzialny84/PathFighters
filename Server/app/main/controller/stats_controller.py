"""
Stats Controller class
"""
from flask_restx import Resource, marshal
from ..dto.stats_to import StatsDto
from ..service.stats_service import *
from flask_jwt_extended import jwt_required

api = StatsDto.api
_stats = StatsDto.stats
_stats_response = StatsDto.stats_response

@api.route('')
class StatsList(Resource):
    # ***GET***
    @api.doc('list_of_all_stats')
    @api.response(200, description="OK", model = _stats)
    @api.response(204, description="NO CONTENT", model = _stats_response)
    @jwt_required()
    def get(self):
        """Get a list of all stats"""
        status_code, stats = api_get_all_stats()
        if stats == None:
            return marshal({'description':'NO CONTENT'}, _stats_response), 204
        else:
            return marshal(stats, _stats), 200

@api.route('/<userid>')
@api.param('userid', 'The userid identifier')
class Stats(Resource):
    # ***GET***
    @api.doc('return_stats_for_user_with_specific_userid.')
    @api.response(200, description="OK", model = _stats)
    @api.response(404, description="NOT FOUND", model = _stats_response)
    @jwt_required()
    def get(self, userid):
        """Get a user with given identifier"""
        status_code, stats = api_get_user_stats(userid)
        if not stats:
            return marshal({'description':'NOT FOUND'}, _stats_response), 404
        else:
            return marshal(stats, _stats), 200

@api.route('/<userid>/add-win')
@api.param('userid', 'The user identifier')
class StatsWins(Resource):
    # ***PATCH***
    @api.doc('add_win_and_total_to_stats_for_user_with_given_username')
    @api.response(200, description="OK", model = _stats_response)
    @api.response(404, description="NOT FOUND", model = _stats_response)
    @jwt_required()
    def patch(self, userid):
        """Patch a wins for user with given identifier"""
        status_code = api_stats_add_win(userid)
        if status_code == 200:
            return marshal({'description':'OK'}, _stats_response), 200
        elif status_code == 404:
            return marshal({'description':'NOT FOUND'}, _stats_response), 404

@api.route('/<userid>/add-fail')
@api.param('userid', 'The user identifier')
class StatsFails(Resource):
    # ***PATCH***
    @api.doc('add_fails_and_total_to_stats_for_user_with_given_username')
    @api.response(200, description="OK", model = _stats_response)
    @api.response(404, description="NOT FOUND", model = _stats_response)
    @jwt_required()
    def patch(self, userid):
        """Patch a fails for user with given identifier"""
        status_code = api_stats_add_fail(userid)
        if status_code == 200:
            return marshal({'description':'OK'}, _stats_response), 200
        elif status_code == 404:
            return marshal({'description':'NOT FOUND'}, _stats_response), 404
            