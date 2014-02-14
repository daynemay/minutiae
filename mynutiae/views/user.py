from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from mynutiae.models._user import (
    DBSession,
    User,
    )
from mynutiae.models._question import Question

@view_config(route_name='login', renderer='mynutiae:templates/login.mako')
def login(request):
    """Login"""
    return {'project': 'mynutiae', 'logged_in': True}

@view_config(route_name='logout', renderer='mynutiae:templates/login.mako')
def logout(request):
    """Logout"""
    return {'project': 'mynutiae... but you logged out'}

@view_config(route_name='user_questions', renderer='mynutiae:templates/user_questions.mako')
def user_questions(request):
    """List all questions TODO: for a user"""
    return { 'questions': Question.all()}
