# coding=utf-8
import os
import sys

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "/..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
# sys.path.append('/home/ysh/mysite')

from mysite import settings
# from mysite import urls
from models import User, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

admin_info = settings.ADMIN_INFO


def initialize():
    engine = create_engine(settings.MYSQL_PATH, encoding='utf-8')
    session_cls = sessionmaker(bind=engine, autocommit=True, expire_on_commit=False)
    session = session_cls()
    Base.metadata.create_all(engine)
    with session.begin():
        result = session.query(User).filter_by(
            username=admin_info['name']).first()
        if result:
            result.passwd = admin_info['passwd']
            result.role = admin_info['role']
            result.email = admin_info['email']
        else:
            user_ref = User()
            user_ref.username = admin_info['name']
            user_ref.passwd = admin_info['passwd']
            user_ref.role = admin_info['role']
            user_ref.email = admin_info['email']
            session.add(user_ref)
    return True

if __name__ == '__main__':
    if initialize():
        print('Initialize db successfully!')
