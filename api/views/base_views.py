from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets


class BaseView(APIView):
    @property
    def help(self):
        return self.__doc__

    @property
    def help_summary(self):
        return ""


class BaseViewSet(viewsets.ViewSet, BaseView):
    pass


class RespMsg(Response):
    """
    Response Message
    """
    def __init__(self, message="Default message.", data=None):
        super(RespMsg, self).__init__()
        self.data = {}
        self.data["success"] = None
        self.data["message"] = message
        self.data["data"] = data


class SuccResponse(RespMsg):
    """
    Success Response Message
    """
    def __init__(self, message="Default success message.", data=None):
        super(SuccResponse, self).__init__(message, data)
        self.data["success"] = 1


class ErrorResponse(RespMsg):
    """
    Error Response Message
    """
    def __init__(self, message="Default error message.", data=None):
        super(ErrorResponse, self).__init__(message, data)
        self.data["success"] = 0
