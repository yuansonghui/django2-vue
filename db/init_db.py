# coding=utf-8

from mysite import settings
from sdsom.db.base import Base
from db.models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

admin_info = settings.ADMIN_INFO


def initialize(args):
    # Master's database
    engine = create_engine(settings.MYSQL_PATH)

    # Enable foreign key
    session_cls = sessionmaker(bind=engine, autocommit=True, expire_on_commit=False)
    session = session_cls()
    Base.metadata.create_all(engine)
    with session.begin():
        result = session.query(User).filter_by(deleted=False).filter_by(
            username=admin_info['name']).first()
        if result:
            result.passwd = admin_info['passwd']
            result.role = admin_info['role']
            result.email = admin_info['email']
        else:
            user_ref = User()
            user_ref.name = admin_info['name']
            user_ref.passwd = admin_info['passwd']
            user_ref.role = admin_info['role']
            user_ref.email = admin_info['email']
    return True

if __name__ == '__main__':
    if initialize():
        print ('Initialize db successfully!')
