from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import generics, permissions
import datetime

from django.utils import timezone

expire_delta = settings.JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']
jwt_payload_handler = settings.JWT_AUTH['JWT_PAYLOAD_HANDLER']
jwt_encode_handler = settings.JWT_AUTH['JWT_ENCODE_HANDLER']
jwt_repsonse_payload_handler = settings.JWT_AUTH['JWT_RESPONSE_PAYLOAD_HANDLER']
User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    status_list = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uri'
        ]
    
    def get_uri(self, obj):
        return f'/api/users/{obj.id}'
    
    def get_status_list(self, obj):
        return f'/api/users/{obj.id}'