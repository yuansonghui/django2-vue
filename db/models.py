from common.base import utcnow
from sqlalchemy import Column, Integer, Boolean, String, DateTime, Text
from db.base import get_session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MysiteBase(object):
    id = Column(Integer, autoincrement=True, primary_key=True)
    status = Column(String(length=255), nullable=True)
    state = Column(String(length=255), nullable=True)
    created_at = Column(DateTime, default=utcnow)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    deleted = Column(Boolean, default=False)

    def __init__(self):
        self._i = None

    # def __iter__(self):
    #     self._i = iter(object_mapper(self).columns)
    #     return self

    def next(self):
        n = self._i.next().name
        return n, getattr(self, n)

    def save(self, session=None):
        """Save this object."""
        if not session:
            session = get_session()
        session.add(self)

    def delete(self, session=None):
        """Delete this object."""
        self.deleted = True
        self.deleted_at = utcnow()
        self.save(session=session)

    def update(self, values):
        """Make the model object behave like a dict."""
        for k, v in values.iteritems():
            setattr(self, k, v)


class User(Base, MysiteBase):
    __tablename__ = 'user'
    username = Column(String(250), nullable=False)
    password = Column(String(64), nullable=False)
    email = Column(String(128), nullable=True)
    role = Column(String(255), default='member')
    phone = Column(String(32), nullable=True)
    remark = Column(Text, nullable=True)

    def __str__(self):
        return '%s' % (self.name)

# class LoginToken(Base):
#     __tablename__ = 'login_token'
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     username = Column(String(64), nullable=False)
#     role = Column(String(255), default='member')
#     token = Column(String(64))
#     # server_dbid = Column(Integer, ForeignKey("sdsom_server.id"), nullable=True)
