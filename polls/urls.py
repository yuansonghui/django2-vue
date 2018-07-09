# -*- coding: utf-8 -*-

from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('question/create', views.QuestionView.create_question),
    path('question/get', views.QuestionView.get_question),
    path('<int:question_id>/', views.detail, name='detail'),
]
