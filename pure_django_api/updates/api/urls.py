"""django_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from .views import (
    UpdateModelDetailAPIView,
    UpdateModelListAPIView,
    UpdateModelCreateAPIView,
    UpdateModelAPIEndpoint
)

urlpatterns = [
    # url(r'^$', UpdateModelListAPIView.as_view()), # List
    url(r'^$', UpdateModelAPIEndpoint.as_view()),
    url(r'^(?P<id>\d+)/$', UpdateModelDetailAPIView.as_view()), # detail view, delete, update view
    url(r'^/create/', UpdateModelCreateAPIView.as_view()), # detail view, delete, update view
    # url(r'^json/serialize4', SerializeListViewClean.as_view()),
]
