from django.contrib import admin
from django.urls import path, re_path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from ..views import UserDetailAPIView, UserStatusAPIView

app_name = 'accounts'

urlpatterns = [
    re_path(r'^(?P<username>\w+)/$', UserDetailAPIView.as_view(), name='detail'),
    re_path(r'^(?P<username>\w+)/status/$', UserStatusAPIView.as_view(), name='status-list'),
]