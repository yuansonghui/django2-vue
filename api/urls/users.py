# -*- coding: utf-8 -*-

from django.urls import path
from django.views.generic.base import TemplateView
from api.views import users

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('list_users', users.UserViewSet.list_users),
    path('create_user', users.UserViewSet.create_user),
]
