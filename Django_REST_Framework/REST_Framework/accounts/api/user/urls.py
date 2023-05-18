from django.contrib import admin
from django.urls import path, re_path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from ..views import AuthView, UserDetailAPIView

app_name = 'api'

urlpatterns = [
    re_path(r'^(?P<username>\w+)/$', UserDetailAPIView.as_view(), name='detail'),
]