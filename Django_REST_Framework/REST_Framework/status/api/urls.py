'''
Adam Forestier
April 26, 2023
'''

from django.contrib import admin
from django.conf.urls import url
from django.urls import (
    include,
    path,
)

from .views import (
    StatusListSearchAPIView,
    StatusCreateAPIView,
    StatusDetailAPIView,
    StatusUpdateAPIView,
    StatusDeleteAPIView,
    StatusAPIView
)

urlpatterns = [
    path('og/', StatusListSearchAPIView.as_view()), # /api/status/og -> List
    path('create/', StatusCreateAPIView.as_view()), # /api/status/create/ -> Create
    path('<int:pk>', StatusDetailAPIView.as_view()), # /api/status/<id>/ -> Detail
    path('<int:pk>/update/', StatusUpdateAPIView.as_view()), # /api/status/<id>/update/ -> Update
    path('<int:pk>/delete/', StatusDeleteAPIView.as_view()), # /api/status/<id>/delete/ -> Delete
    path('', StatusAPIView.as_view()) # ULTIMATE ENDPOINT!
]