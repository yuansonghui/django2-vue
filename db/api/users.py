from db import models
from db.base import get_session, model_query


# def list_users(all=False):
#     result = []
#     user_querys = model_query(models.User).all()
#     for item in user_querys:
#         user = {}
#         user['id'] = item.id
#         user['name'] = item.username
#         user['email'] = item.email
#         user['role'] = item.role
#         user['phone'] = item.phone
#         if all:
#             user['created_at'] = item.created_at
#             user['deleted_at'] = item.deleted_at
#             user['deleted'] = item.deleted
#             user['status'] = item.status
#             user['state'] = item.state
#             user['updated_at'] = item.updated_at
#         result.append(user)
#     return result


# def create_user(name, password, email='', role='member', phone=''):
#     session = get_session()
#     user = model_query(models.User).filter_by(username=name).first()
#     if user:
#         return 0, 'User name is exist!'
#     with session.begin():
#         user_ref = models.User()
#         user_ref.username = name
#         user_ref.passwd = password
#         user_ref.email = email
#         user_ref.role = role
#         user_ref.phone = phone
#         session.add(user_ref)
#     return 1, 'Create user successfully!'


def user_authenticate(username, password):
    user = model_query(models.User).filter_by(username=username, password=password).first()
    if user:
        return True
    return False


# def get_user_token(username):
#     user = model_query(models.LoginToken).filter_by(username=username).first()
#     if user:
#         return user.token
#     return ''


# def set_user_token(username, role, token):
#     session = get_session()
#     with session.begin():
#         user = model_query(models.LoginToken).filter_by(username=username).first()
#         if user:
#             user.token = token
#             user.role = role
#         else:
#             token_ref = models.LoginToken()
#             token_ref.token = token
#             token_ref.username = username
#             token_ref.role = role
#             session.add(token_ref)
#     return True
