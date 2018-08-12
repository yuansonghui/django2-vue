"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path(r'admin/', admin.site.urls),
    path(r'api/user/', include('api.urls.users')),
    path(r'api/login/', obtain_jwt_token),
]
