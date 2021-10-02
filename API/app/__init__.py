from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.stats_controller import api as stats_ns


blueprint = Blueprint('api', __name__)
# authorizations = {
#     'apikey': {
#         'type': 'apiKey',
#         'in': 'header',
#         'name': 'Authorization'
#     }
# }

api = Api(
    blueprint,
    title='Engineering Thesis API',
    version='1.0',
    description='Api created for Engineering Thesis'
    # authorizations=authorizations,
    # security='apikey'
)

api.add_namespace(user_ns, path='/users')
api.add_namespace(stats_ns, path='/stats')

