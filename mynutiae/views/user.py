from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from models import (
    DBSession,
    MyModel,
    )

@view_config(route_name='login', renderer='templates/login.pt')
def login(request):
    """Login"""
    return {'project': 'mynutiae'}

@view_config(route_name='logout', renderer='templates/login.pt')
def login(request):
    """Logout"""
    return {'project': 'mynutiae... but you logged out'}
