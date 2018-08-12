import hashlib
import time

# from rest_framework.decorators import api_view
# from django.views.decorators.csrf import ensure_csrf_cookie
# from django.contrib.auth import get_user_model, authenticate, login as auth_login, logout as auth_logout

from api.views.base_views import SuccResponse, ErrorResponse, BaseViewSet
from django.contrib.auth.models import User
# from db.api import users as db_users


class UserViewSet(BaseViewSet):
    """docstring for UserViewSet"""

    def __init__(self, *args, **kwargs):
        super(UserViewSet, self).__init__(*args, **kwargs)

    def list_users(self, request):
        result = []
        user_query = User.objects.all()
        for item in user_query:
            user = {}
            user['id'] = item.id
            user['username'] = item.username
            user['is_active'] = item.is_active
            user['email'] = item.email
            user['roles'] = ['superuser'] if item.is_superuser else ['member']
            result.append(user)
        return SuccResponse(data=result)

    def get_user(self, request):
        item = User.objects.filter(username=request.user.username).first()
        user = {}
        user['id'] = item.id
        user['username'] = item.username
        user['is_active'] = item.is_active
        user['email'] = item.email
        user['roles'] = ['superuser'] if item.is_superuser else ['member']
        return SuccResponse(data=user)

    def logout(self, request):
        return SuccResponse()
