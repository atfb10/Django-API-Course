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