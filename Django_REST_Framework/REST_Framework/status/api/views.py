'''
Adam Forestier
May 17, 2023
'''
from django.shortcuts import get_object_or_404
import json
from rest_framework.authentication import SessionAuthentication
from rest_framework import (generics, mixins, permissions) # Generics are unbelievably good
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from accounts.api.permissions import IsOwnerOrReadOnly
from .serializers import StatusSerializer
from status.models import Status

def is_json(data) -> bool:
    try:
        js = json.loads(data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid

# List
class StatusListSearchAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        '''
        http get!
        '''
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        json_data = serializer.data
        return Response(json_data)


# Create!
class StatusCreateAPIView(generics.CreateAPIView):
    # NOTE: Great googly moogly this is easy
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def perform_create(self, serializer):
        '''
        override perform_create() method to enforce that when creating a post, user cannot be selected. user is the user using the endpoint
        NOTE: Can override this method to enfore serializer to save in a certain way!
        '''
        serializer.save(user=self.request.user)

# Detail
class StatusOnlyDetailAPIView(generics.RetrieveAPIView):
    # Unbelievably easy!
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    # NOTE: change the name of the lookup field. NOTICE it is pk by default. For the detail view in status/api/urls.py see you have put in pk! If you want to call it something else, this is the way!
    # lookup_field = 'id' # works w/ 'slug'

    # NOTE: Perform by overwriting get_object() method!
    # def get_object(self, *args, **kwargs):
    #     kwargs = self.kwargs
    #     kw_id = kwargs.get('id') # NOTE: This works great!!! Just need to change "pk" to "id" in status/api/urls.py in detail view :) 
    #     return Status.objects.get(pk=kw_id)

# Update
class StatusUpdateAPIView(generics.UpdateAPIView):
    # Unbelievably easy!
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer 

# Delete
class StatusDeleteAPIView(generics.DestroyAPIView):
    # Unbelievably easy!
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer 



# One to rule create and list
class StatusAPIView(generics.ListAPIView, mixins.CreateModelMixin):

    # Assigment
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [SessionAuthentication] # NOTE: Commented out to show that the default auth & permissions are working due to what is in main.py and important * from main.py in settings.py!
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    passed_id = None
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('user__username', 'content')
    ordering_fields = ('user__username', 'timestamp')
    queryset = Status.objects.all()

    # NOTE: get_queryset has been improved through search fields and filter backends
    # def get_queryset(self):
    #     '''
    #     overwrite the default queryset to be able to search by content!
    #     NOTE: search by /api/status/?q=<text to search>
    #     '''
    #     qs = Status.objects.all()
    #     q = self.request.GET.get('q')
    #     if q is not None:
    #         qs = qs.filter(content__icontains=q)
    #     return qs
    
    # Create
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    # Create
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

# One to rule detail, delete, update
class StatusDetailAPIView(generics.RetrieveAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    # Detail
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    authentication_classes = [SessionAuthentication]
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    # update
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    # Delete
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
# NOTE: UNLIMITED POWER!!!!!!!!!!!! # NOTE: Ultimate endpoints with extreme ease
class UltimateStatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_class = [SessionAuthentication]
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    

class UltimateStatusAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_class = [SessionAuthentication]
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('user__username', 'content')
    ordering_fields = ('user__username', 'timestamp')

    # Create
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


'''
one endpoint to do all. NOTE: Not best in practice. Gets overally complex. Do 2, 1 detail (update, detail, delete), 1 list (list, create)
'''
class OneEndpointAPIView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.ListAPIView):
    permission_classes = []
    authentication_class = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    passed_id = None

    def get_queryset(self):
        # List view. Allow for querying w/ q
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs
    
    def get_object(self):
        '''
        get object by id if it exists. get specific id by: status/?=<id>
        '''
        request = self.request
        passed_id = request.GET.get('id', None) or self.passed_id
        qs = self.get_queryset()
        obj = None
        if passed_id:
            obj = get_object_or_404(qs, id=passed_id)
            self.check_object_permissions(request, obj) # check object permissions is built in method for Retrieve mixin class
        return obj
    
    def perform_destroy(self, instance):
        if instance is not None:
            return instance.delete()
        return None

    def get(self, request, *args, **kwargs):
        '''
        override default get. get specific id by: status/?id=<id>
        '''
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body = request.body
        
        if is_json(body):
            json_data = json.loads(request.body)
        
        new_passed_id = json_data.get('id', None)
        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = passed_id
        if passed_id is not None:
            return self.retrieve(request, *args, **kwargs) # retrieve is built in method for Retrieve mixin class
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Create
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body = request.body
        
        if is_json(body):
            json_data = json.loads(request.body)
        
        new_passed_id = json_data.get('id', None)
        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = passed_id
        # update
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body = request.body
        
        if is_json(body):
            json_data = json.loads(request.body)
        
        new_passed_id = json_data.get('id', None)
        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = passed_id
        # update
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        # delete
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body = request.body
        
        if is_json(body):
            json_data = json.loads(request.body)
        
        new_passed_id = json_data.get('id', None)
        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = passed_id
        return self.destroy(request, *args, **kwargs)