from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from mynutiae.models.models import (
    DBSession,
    User,
    )

@view_config(route_name='login', renderer='mynutiae:templates/login.mako')
def login(request):
    """Login"""
    return {'project': 'mynutiae', 'logged_in': True}

@view_config(route_name='logout', renderer='mynutiae:templates/login.mako')
def logout(request):
    """Logout"""
    return {'project': 'mynutiae... but you logged out'}
