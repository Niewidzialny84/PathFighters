from flask_restx import Api
from flask import Blueprint

from .main.controller.login_controller import api as login_ns
# from .main.controller.registration_controller import api as register_ns
# from .main.controller.stats_controller import api as stats_ns


blueprint = Blueprint('server', __name__)
# authorizations = {
#     'apikey': {
#         'type': 'apiKey',
#         'in': 'header',
#         'name': 'Authorization'
#     }
# }

server = Api(
    blueprint,
    title='Engineering Thesis Server',
    version='1.0',
    description='Server created for Engineering Thesis'
    # authorizations=authorizations,
    # security='apikey'
)

server.add_namespace(login_ns, path='/login')
# server.add_namespace(register_ns, path='/register')
# server.add_namespace(stats_ns, path='/stats')