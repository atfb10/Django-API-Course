'''
Adam Forestier
April 26, 2023
'''
from rest_framework import generics # Generics are unbelievably good
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import StatusSerializer
from status.models import Status

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
class StatusDetailAPIView(generics.RetrieveAPIView):
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



# One to rule them all
class StatusAPIView(generics.ListAPIView):

    # Assigment
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get_queryset(self):
        '''
        overwrite the default queryset to be able to search by content!
        NOTE: search by /api/status/?q=<text to search>
        '''
        qs = Status.objects.all()
        q = self.request.GET.get('q')
        if q is not None:
            qs = qs.filter(content__icontains=q)
        return qs
    