# -*- coding: utf-8 -*-

from django.urls import path
from django.views.generic.base import TemplateView
from api.views import users

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('list_users', users.UserViewSet.as_view({'get': 'list_users'})),
    path('info', users.UserViewSet.as_view({'get': 'get_user'})),
    path('logout', users.UserViewSet.as_view({'post': 'logout'})),
]
