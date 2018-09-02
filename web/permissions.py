from rest_framework.permissions import IsAuthenticated
from db.api import users as db_users
from common import base
from mysite import settings

TOKEN_LIFE_TIME = settings.TOKEN_LIFE_TIME


def check_token(token):
    token_info = db_users.get_token_info(token)
    if not token_info:
        return False
    residue_time = base.utcnow().timestamp() - token_info['created_at'].timestamp()
    if residue_time > TOKEN_LIFE_TIME:
        print(residue_time)
        return False
    return True


class MyIsAuthenticated(IsAuthenticated):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        if request._request.path == '/api/user/logout':
            return True
        token = request.META.get('HTTP_X_TOKEN')
        ret = check_token(token)
        return ret
