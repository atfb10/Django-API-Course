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
from django.conf.urls import url, include
from django.contrib import admin

from updates.views import (
    json_example_view,
    JsonCBV,
    JsonCVB2,
    SerializeDetailViewEx,
    SerializeListViewEx,
    SerializeDetailViewClean,
    SerializeListViewClean
)

from updates.api.views import UpdateModelListAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^json/example0', json_example_view),
    url(r'^json/example1', JsonCBV.as_view()),
    url(r'^json/example2', JsonCVB2.as_view()),
    url(r'^json/serialize1', SerializeDetailViewEx.as_view()),
    url(r'^json/serialize2', SerializeListViewEx.as_view()),
    url(r'^json/serialize3', SerializeDetailViewClean.as_view()),
    url(r'^json/serialize4', SerializeListViewClean.as_view()),
    url(r'^json/serialize5', UpdateModelListAPIView.as_view()),

    # Cleaner implementation -> with API sub-directory ^ is saved purely for reference
    url(r'^api/updates/', include('updates.api.urls')), # api/updates/ --> list api/updates/1/ --> detail view
]
