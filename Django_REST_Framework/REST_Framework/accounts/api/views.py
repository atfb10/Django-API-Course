from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from rest_framework.views  import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions

from .serializers import UserRegisterSerializer
from ..api.user.serlializers import UserDetailSerializer
from .permissions import AnonymousPermission

jwt_payload_handler = settings.JWT_AUTH['JWT_PAYLOAD_HANDLER']
jwt_encode_handler = settings.JWT_AUTH['JWT_ENCODE_HANDLER']
jwt_repsonse_payload_handler = settings.JWT_AUTH['JWT_RESPONSE_PAYLOAD_HANDLER']

User = get_user_model()

class UserDetailAPIView(generics.RetrieveAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.filter(is_active=True)
    lookup_field = 'username'

# Custom authentication view
class AuthView(APIView):
    permission_classes = [AnonymousPermission]
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return Response({'Detail': 'You are already authenticated'}, status=400)
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username, password)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        response = jwt_repsonse_payload_handler(token, user, request)
        return Response(response)
    
# Register user view
class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AnonymousPermission]

    def get_serializer_context(self, *args, **kwargs):
        return {"Request": self.request}