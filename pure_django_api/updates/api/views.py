'''
adam forestier
april 22, 2023
'''
import json
from django.views.generic import View
from django.http import HttpResponse

from django_api.mixins import HttpResponseMixin
from updates.models import Update
from updates.forms import UpdateModelForm
from updates.api.utils import is_json



# Update, Delete, Retrive (CRUD) -- Perform Crud for single object of Update model. Example. NOTE: 1 endpoint version at bottom of the page
class UpdateModelDetailAPIView(View, HttpResponseMixin):
    '''
    retrieve, update, delete for single object
    '''
    def get_object(self, id=None):
        try:
            obj = Update.objects.get(id=id)

        except Update.DoesNotExist:
            obj = None

        return obj
    
    def get(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)

        if obj is None:
            error_data = json.dumps({'Error Message': 'Data Not Found'})
            self.render_to_response(error_data, status=404)

        json_data = obj.serialize()    
        self.render_to_response(json_data)
    
    def put(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        create_status = 201
        error_status = 400

        if obj is None:
            error_data = json.dumps({'Error Message': 'Data Not Found'})
            self.render_to_response(error_data, status=404)
        new_data = request.body

        if not is_json(new_data):
            error_data = json.dumps({'Error Message': 'Data Not in JSON Format'})
            self.render_to_response(error_data, status=400)

        data = json.loads(obj.serialize())
        passed_data = json.loads(request.body)
        for key, val in passed_data.items():
            data[key] = val
        form = UpdateModelForm(data=data, instance=obj)

        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data, create_status)
        
        elif form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, error_status)
        
        json_data = json.dumps({'message': 'something went wrong'})
        self.render_to_response(json_data, error_status)


    def delete(self, id, request, *args, **kwargs):
        obj = self.get_object(id=id)

        if obj is None:
            error_data = json.dumps({'Error Message': 'Data Not Found'})
            self.render_to_response(error_data, status=404)

        deleted = obj.delete()
        if deleted:
            json_data = json.dumps({'message': 'successfully deleted'})
            return self.render_to_response(json_data)

        error_data = json.dumps({'Error Message': 'Could not delete'})
        self.render_to_response(error_data, status=400)

class UpdateModelListAPIView(View, HttpResponseMixin):
    '''
    list view Example. NOTE: One endpoint version at bottom of page
    '''
    # def render_to_response(data, status=200):
    #     '''
    #     make it so I don't have to type this out everytime
    #     '''
    #     return HttpResponse(data, content_type='application/json', status=status)
    is_json = True
    def get(self, request, *args, **kwargs):
        json_data = Update.objects.all().serialize()
        self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        data = json.dumps({"message": "you cannot create an entire list. Please the /api/updates/create/ api endpoint"})
        my_status = 400 # bad request
        self.render_to_response(data, my_status)

    def delete(self, request, *args, **kwargs):
        data = json.dumps({"message": "you cannot delete all data!"})
        my_status = 403 # status saying not allowed - forbidden status
        return self.render_to_response(data, my_status)

class UpdateModelCreateAPIView(View):
    '''
    create view. Example. NOTE: 1 endpoint at bottom of page
    '''
    is_json = True
    def post(self, request, *args, **kwargs):
        create_status = 201 # 201 is a status code that indicates creation
        error_status = 400
        if not is_json(request.body):
            error_data = json.dumps({'message': 'error occurred'})
            return self.render_to_response(error_data, error_status)
        form = UpdateModelForm(json.loads(request.body))

        if form.is_valid():
            obj = form.save(commit=True)
            obj = obj.serialize()
            return self.render_to_response(obj, create_status)
        
        elif form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, error_status)
        
        data = json.dumps({'message': 'error occurred'})
        return self.render_to_response(data, error_status)
    
class UpdateModelAPIEndpoint(View, HttpResponseMixin):
    is_json = True
    queryset = None

    def get_queryset(self):
        qs = Update.objects.all()
        self.queryset = qs 
        return qs
    
    def get_object(self, id):
        if id == None:
            return None
        qs = self.get_queryset().filter(id=id)
        if qs:
            return qs.first()
        return None
    
    def get(self, request, *args, **kwargs):
        json_data = self.get_queryset().serialize()
        self.render_to_response(json_data)
    
    def post(self, request, *args, **kwargs):
        create_status = 201 # 201 is a status code that indicates creation
        error_status = 400
        if not is_json(request.body):
            error_data = json.dumps({'message': 'error occurred'})
            return self.render_to_response(error_data, error_status)
        form = UpdateModelForm(json.loads(request.body))

        if form.is_valid():
            obj = form.save(commit=True)
            obj = obj.serialize()
            return self.render_to_response(obj, create_status)
        
        elif form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, error_status)
        
        data = json.dumps({'message': 'error occurred'})
        return self.render_to_response(data, error_status)
    
    def put(self, request, *args, **kwargs):
        create_status = 201
        error_status = 400
        new_data = request.body

        if not is_json(new_data):
            error_data = json.dumps({'Error Message': 'Data Not in JSON Format'})
            self.render_to_response(error_data, status=400)
        
        passed_data = json.loads(new_data)
        passed_id = passed_data.get('id', None)
        obj = self.get_object(id=passed_id)

        if obj is None:
            error_data = json.dumps({'Error Message': 'Object Not Found'})
            self.render_to_response(error_data, status=404)

        # json_data = obj.serialize()

        data = json.loads(obj.serialize())
        for key, val in passed_data.items():
            data[key] = val
        form = UpdateModelForm(data=data, instance=obj)

        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data, create_status)
        
        elif form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, error_status)
        
        json_data = json.dumps({'message': 'something went wrong'})
        self.render_to_response(json_data, error_status)

    def delete(self, id, request, *args, **kwargs):
        new_data = request.body

        if not is_json(new_data):
            error_data = json.dumps({'Error Message': 'Data Not in JSON Format'})
            self.render_to_response(error_data, status=400)

        passed_data = json.loads(new_data)
        passed_id = passed_data.get('id', None)
        obj = self.get_object(id=passed_id)
        if obj is None:
            error_data = json.dumps({'Error Message': 'Data Not Found'})
            self.render_to_response(error_data, status=404)

        deleted = obj.delete()
        if deleted:
            json_data = json.dumps({'message': 'successfully deleted'})
            return self.render_to_response(json_data)

        error_data = json.dumps({'Error Message': 'Could not delete'})
        self.render_to_response(error_data, status=400)