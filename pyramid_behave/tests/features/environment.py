from pyramid import testing
from pyramid.paster import get_appsettings
from sqlalchemy import engine_from_config

from pyramid_behave.models import (
    Base,
    DBSession,
    )

def before_all(context):
    context.settings = get_appsettings('test.ini')
    context.engine = engine_from_config(context.settings, 'sqlalchemy.')

def before_scenario(context, scenario):
    context.configurator = testing.setUp(request=testing.DummyRequest(),
                                         settings=context.settings)
    Base.metadata.create_all(context.engine)
    DBSession.configure(bind=context.engine)
    context.db = DBSession

def after_scenario(context, scenario):
    testing.tearDown()
    context.db.remove()
