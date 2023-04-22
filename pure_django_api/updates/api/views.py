'''
adam forestier
april 22, 2023
'''

from django.views.generic import View
from django.http import HttpResponse

from django_api.mixins import HttpResponseMixin
from updates.models import Update

# Update, Delete, Retrive (CRUD) -- Perform Crud for single object of Update model
class UpdateModelDetailAPIView(View, HttpResponseMixin):
    '''
    retrieve, update, delete for single object
    '''
    def get(self, request, id, *args, **kwargs):
        json_data = Update.objects.get(id=id).serialize()
        self.render_to_response(json_data)
    
    def put(self, request, *args, **kwargs):
        json_data = {}
        self.render_to_response(json_data)

    def delete(self, request, *args, **kwargs):
        json_data = {}
        self.render_to_response(json_data)

class UpdateModelListAPIView(View, HttpResponseMixin):
    '''
    list view
    '''
    is_json = True
    def render_to_response(data, status=200):
        '''
        make it so I don't have to type this out everytime
        '''
        return HttpResponse(data, content_type='application/json', status=status)
    
    def get(self, request, *args, **kwargs):
        json_data = Update.objects.all().serialize()
        self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        data = {"message": "you cannot create an entire list"}
        my_status = 400 # bad request
        self.render_to_response(data, my_status)

    def delete(self, request, *args, **kwargs):
        data = {"message": "you cannot delete all data!"}
        my_status = 403 # status saying not allowed - forbidden status
        return self.render_to_response(data, my_status)

class UpdateModelCreateAPIView(View):
    '''
    create view
    '''
    def post(self, request, *args, **kwargs):
        json_data = {}
        my_status = 201 # 201 is a status code that indicates creation
        return HttpResponse(json_data, content_type='application/json')