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
    StatusOnlyDetailAPIView,
    StatusUpdateAPIView,
    StatusDeleteAPIView,
    StatusAPIView,
    StatusDetailAPIView,
    UltimateStatusDetailAPIView,
    UltimateStatusAPIView,
    OneEndpointAPIView
)

app_name = "status"

urlpatterns = [
    # path('og/', StatusListSearchAPIView.as_view()), # /api/status/og -> List
    # path('create/', StatusCreateAPIView.as_view()), # /api/status/create/ -> Create
    # path('old/<int:pk>', StatusOnlyDetailAPIView.as_view()), # /api/status/old/<id>/ -> Detail
    # path('<int:pk>/update/', StatusUpdateAPIView.as_view()), # /api/status/<id>/update/ -> Update
    # path('<int:pk>/delete/', StatusDeleteAPIView.as_view()), # /api/status/<id>/delete/ -> Delete
    path('detail/<int:pk>', StatusDetailAPIView.as_view(), name='detail'), # NOTE: DETAIL ENDPOINT: -> Detail, Update, Delete (with mixins)
    path('<int:pk>', UltimateStatusDetailAPIView.as_view(), name='detail1'), # NOTE: ULTIMATE DETAIL ENDPOINT: -> Detail, Update, Delete (with incredible built in class)
    path('status/', StatusAPIView.as_view()), # NOTE:  LIST ENDPOINT! -> List & Create (with mixins)
    path('', UltimateStatusAPIView.as_view()), # NOTE: ULTIMATE LIST ENDPOINT! -> List & Create (with incredible built in class)
    path('single_endpoint/', OneEndpointAPIView.as_view()) # NOTE: One endpoint that handles absolutely everything!
]