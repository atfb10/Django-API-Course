from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from rest_framework.views  import APIView
from rest_framework.response import Response
from rest_framework import permissions

jwt_payload_handler = settings.JWT_AUTH['JWT_PAYLOAD_HANDLER']
jwt_encode_handler = settings.JWT_AUTH['JWT_ENCODE_HANDLER']
jwt_repsonse_payload_handler = settings.JWT_AUTH['JWT_RESPONSE_PAYLOAD_HANDLER']


# Custom authentication view
class AuthView(APIView):
    permission_classes = [permissions.AllowAny]
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