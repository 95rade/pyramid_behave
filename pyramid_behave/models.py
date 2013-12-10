from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Todo(Base):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    task = Column(Text)
    completed = Column(Boolean)

