from pyramid.view import view_config

from .models import (
    DBSession,
    Todo,
    )


@view_config(route_name='todo', renderer='todo.mako')
def todo(request):
    todo = DBSession.query(Todo).filter(Todo.id == request.matchdict['id']).one()
    return {'todo':todo}

