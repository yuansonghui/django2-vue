import hashlib
import time
import uuid

from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

from api.views.base_views import SuccResponse, ErrorResponse, BaseViewSet
from db.api import users as db_users

@api_view(['POST'])
@permission_classes((AllowAny,))
@csrf_exempt
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    ret = db_users.user_authenticate(username, password)
    if ret:
        token = uuid.uuid4().hex
        db_users.set_token(username, token)
        return Response({'token': token})
    return ErrorResponse('登录失败!')

class UserViewSet(BaseViewSet):
    """docstring for UserViewSet"""

    def __init__(self, *args, **kwargs):
        super(UserViewSet, self).__init__(*args, **kwargs)

    def list_users(self, request):
        """
        获取所有用户信息
        """
        # result = []
        # user_query = User.objects.all()
        # for item in user_query:
        #     user = {}
        #     user['id'] = item.id
        #     user['username'] = item.username
        #     user['is_active'] = item.is_active
        #     user['email'] = item.email
        #     user['roles'] = ['superuser'] if item.is_superuser else ['member']
        #     result.append(user)
        return SuccResponse()

    def get_user(self, request):
        """
        获取登录用户信息, 包括用户名, 邮箱, 角色等.
        """
        # item = User.objects.filter(username=request.user.username).first()
        # user = {}
        # user['id'] = item.id
        # user['username'] = item.username
        # user['is_active'] = item.is_active
        # user['email'] = item.email
        # user['roles'] = ['superuser'] if item.is_superuser else ['member']
        return SuccResponse()

    def logout(self, request):
        """
        注销用户
        """
        try:
            token = request.META['HTTP_X_TOKEN']
            db_users.delete_token(token)
            return SuccResponse()
        except:
            return SuccResponse()

    def create_user(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email', '')
        if not username or not password:
            return ErrorResponse('username and password is required!')
        User.objects.create_user(username=username, password=password, email=email)
        return SuccResponse()
         
