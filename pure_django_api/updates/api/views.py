'''
adam forestier
april 22, 2023
'''

from django.views.generic import View
from django.http import HttpResponse

from updates.models import Update

# Update, Delete, Retrive (CRUD) -- Perform Crud for single object of Update model
class UpdateModelDetailAPIView(View):
    '''
    retrieve, update, delete for single object
    '''
    def get(self, request, id, *args, **kwargs):
        json_data = Update.objects.get(id=id).serialize()
        return HttpResponse(json_data, content_type='application/json')
    
    def put(self, request, *args, **kwargs):
        json_data = {}
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        json_data = {}
        return HttpResponse(json_data, content_type='application/json')

class UpdateModelListAPIView(View):
    '''
    list view
    '''
    def get(self, request, *args, **kwargs):
        json_data = Update.objects.all().serialize()
        return HttpResponse(json_data, content_type='application/json')
    
    def post(self, request, *args, **kwargs):
        json_data = {}
        return HttpResponse(json_data, content_type='application/json')
    
class UpdateModelCreateAPIView(View):
    '''
    create view
    '''
    def post(self, request, *args, **kwargs):
        json_data = {}
        return HttpResponse(json_data, content_type='application/json')