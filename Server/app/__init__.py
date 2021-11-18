from flask_restx import Api
from flask import Blueprint

from .main.controller.login_controller import api as login_ns
from .main.controller.logout_controller import api as logout_ns
from .main.controller.users_controller import api as users_ns
from .main.controller.registration_controller import api as register_ns
from .main.controller.stats_controller import api as stats_ns
from .main.controller.refresh_token_controller import api as refresh_ns

blueprint = Blueprint('server', __name__)

server = Api(
    blueprint,
    title='Engineering Thesis Server',
    version='1.0',
    description='Server created for Engineering Thesis'
)

server.add_namespace(login_ns, path='/login')
server.add_namespace(logout_ns, path='/logout')
server.add_namespace(users_ns, path='/user')
server.add_namespace(register_ns, path='/register')
server.add_namespace(stats_ns, path='/stats')
server.add_namespace(refresh_ns, path='/refresh')