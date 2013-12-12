from behave import (
    given,
    when,
    then,
    )

from sqlalchemy import engine_from_config
from pyramid.paster import get_appsettings

from pyramid_behave.models import (
    Base,
    DBSession,
    Todo
    )

@given(u'my task is "new todo task"')
def step_impl(context):
    config_uri = 'development.ini'
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    context.db = DBSession

@when(u'I create a new todo entry')
def step_impl(context):
    todo = Todo(task=context.text, completed=False)
    context.db.add(todo)
    context.db.flush()
    context.todo = todo

@then(u'I should find todo in todo table')
def step_impl(context):
    todo = context.db.query(Todo).get(context.todo.id)
    assert todo
