from common.base import utcnow
from sqlalchemy import Column, Integer, BigInteger, Float, Boolean, String, Text, DateTime, ForeignKey, Table, Index
from sqlalchemy.orm import relationship, backref
from db.base import Base, get_session


class MysiteBase(object):
    id = Column(Integer, autoincrement=True, primary_key=True)
    created_at = Column(DateTime, default=utcnow)
    updated_at = Column(DateTime, default=utcnow)
    deleted_at = Column(DateTime, default=utcnow)

    def __init__(self):
        self._i = None

    def __iter__(self):
        self._i = iter(object_mapper(self).columns)
        return self

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


class User(MysiteBase):
    name = Column(String(length=64), nullable=False, unique=True)
    passwd = Column(String(length=64), nullable=False)
    email = Column(String(length=128), nullable=True)
    role = Column(String(max_length=255), default='member')
    token = Column(String(max_length=255), nullable=True)
    phone = Column(String(max_length=32), nullable=True)

    def __str__(self):
        return '%s' % (self.name)

    def get_token(self):
        return '%s:%s' % (self.name, self.token)
