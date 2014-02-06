""" Application user model """

from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Unicode,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    synonym,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

def hash_password(password):
    """ TODO: actually hash password"""
    return password

class User(Base):
    """ Application's user model.  """
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(Unicode(20), unique=True)
    name = Column(Unicode(50))
    email = Column(Unicode(50))
    _password = Column('password', Unicode(60))

    def _get_password(self):
        """Private password getter"""
        return self._password

    def _set_password(self, password):
        """Private password setter"""
        self._password = hash_password(password)

    password = property(_get_password, _set_password)
    password = synonym('_password', descriptor=password)

    def __init__(self, username, password, name, email):
        self.username = username
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def get_by_username(cls, username):
        """ TODO: Docstring"""
        return DBSession.query(cls).filter(cls.username == username).first()

    @classmethod
    def check_password(cls, username, password):
        """TODO: docstring"""
        user = cls.get_by_username(username)
        if not user:
            return False
#         return crypt.check(user.password, password)
# TODO: actually check password
        return True        

# TODO: Other indexes
Index('my_index', User.email, unique=True, mysql_length=255)

# TODO: Use as basis for n:m relationship tables
# ideas_tags = Table('ideas_tags', Base.metadata,
#    Column('idea_id', Integer, ForeignKey('ideas.idea_id')),
#    Column('tag_id', Integer, ForeignKey('tags.tag_id'))
# )
