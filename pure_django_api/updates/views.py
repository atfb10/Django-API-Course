'''
author: Adam Forestier
last updated: april 22, 2023
IMPORTANT NOTE: This views page is just used as example, building up to cleanest implementation. API views should be in own foldre titled "api" within the app and that folder should contain an __init__.py and views.py -> where api views are housed
'''

import json

from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View

from .models import Update
from django_api.mixins import JsonResponseMixin

# def detail_view(request):
#     '''
#     return json data
#     '''
#     return render()

def json_example_view(request):
    '''
    function based view example
    python dictionary turns into JSON object
    URI
    '''
    data = {
        'count': 1000,
        'content': 'content example'
    }
    return JsonResponse(data=data)


class JsonCBV(View):
    '''
    class based view example
    '''
    def get(self, request, *args, **kwargs):
        data = {
            'count': 100,
            'content': 'Hi there'
        }
        return JsonResponse(data=data)
    
class JsonCVB2(JsonResponseMixin, View):
    '''
    class based view w/ example of using class mixin
    '''
    def get(self, request, *args, **kwargs):
        '''
        would already have data cleansed from get_data & returned as json object
        '''
        data = {
            'count': 121,
            'content': 'Howdy'
        }
        return self.render_to_json_response(context=data)
    
class SerializeDetailViewEx(View):
    '''
    actually get data frame database
    '''
    def get(self, request, *args, **kwargs):
        '''
        hardcoded example of single
        '''
        obj = Update.objects.get(id=1)
        data = serialize(format='json', queryset=[obj,], fields=('user', 'content')) # specify which fields you want returned
        return HttpResponse(data, content_type='application/json')
    
class SerializeListViewEx(View):
    '''
    view all items for model with fields specified
    '''
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        data = serialize(format='json', queryset=qs)
        return HttpResponse(data, content_type='application/json')
    
class SerializeDetailViewClean(View):
    '''
    less re-writing using managers!
    '''
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        data = obj.serialize()
        return HttpResponse(data, content_type='application/json')

class SerializeListViewClean(View):
    '''
    less re-writing using managers!
    '''
    def get(self, request, *args, **kwargs):
        data = Update.objects.all().serialize()
        return HttpResponse(data, content_type='application/json')