from behave import (
    given,
    when,
    then,
    )

from pyramid import testing
from pyramid_behave.models import Todo

@given(u'my todo is {task}')
def step_impl(context, task):
    context.todo = Todo(task=task, completed=False)

@when(u'I create a new todo entry')
def step_impl(context):
    context.db.add(context.todo)
    context.db.flush()

@then(u'I should find todo in todo table')
def step_impl(context):
    todo = context.db.query(Todo).get(context.todo.id)
    assert todo

@when(u'I visit the URL /{id}')
def step_impl(context,id):
    from pyramid_behave.views import todo
    context.configurator.add_route('/','/{id:\d+}')
    request = testing.DummyRequest()
    request.matchdict['id'] = int(id)
    context.result = todo(request)

@then(u'I should see my todo')
def step_impl(context):
    assert context.result['todo']
