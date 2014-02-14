"""
Model representing a question defined by a user
"""
import sqlalchemy
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Unicode,
    )

# from sqlalchemy.ext.declarative import declarative_base

from mynutiae import Base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    synonym,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
# Base = declarative_base()

def hash_password(password):
    """ TODO: actually hash password"""
    return password

class Question(Base):
    """ Question model.  """
    __tablename__ = 'questions'
    question_id = Column(Integer, primary_key=True)
    # TODO: Figure out foreign key
    owner_id = Column(Integer, primary_key=True)
    question_text = Column(Unicode(140), unique=True)

    def __init__(self, owner_id, question_text):
        self.owner = owner_id
        self.question_text = question_text

    @classmethod
    def all(cls):
        print dir(DBSession)
        return DBSession.query(Question).order_by(sqlalchemy.desc(Question.question_text))

    @classmethod
    def by_id(cls, id):
        return DBSession.query(Question).filter(Question.question_id == id).first()

# TODO: Other indexes
Index('question_text_index', Question.question_text, mysql_length=255)

# TODO: Use as basis for n:m relationship tables
# ideas_tags = Table('ideas_tags', Base.metadata,
#    Column('idea_id', Integer, ForeignKey('ideas.idea_id')),
#    Column('tag_id', Integer, ForeignKey('tags.tag_id'))
# )
