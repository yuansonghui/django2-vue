from rest_framework.decorators import api_view
from api.views.base_views import SuccResponse, ErrorResponse, BaseViewSet
from db.api import users


class UserViewSet(BaseViewSet):
    """docstring for UserViewSet"""

    @api_view(['GET'])
    def list_users(request):
        result = users.list_users()
        return SuccResponse(data=result)

    @api_view(['POST'])
    def create_user(request):
        data = request.data
        name = data.get('name')
        password = data.get('password')
        email = data.get('email')
        role = data.get('role')
        phone = data.get('phone')
        if not name or not password:
            return ErrorResponse('Name and password is requested!')
        code, message = users.create_user(name, password, email, role, phone)
        if code == 0:
            return ErrorResponse(message=message)
        elif code == 1:
            return SuccResponse(message=message)
