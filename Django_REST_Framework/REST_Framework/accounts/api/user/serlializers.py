from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import generics, permissions
import datetime
from django.utils import timezone
from rest_framework.reverse import reverse as api_reverse
from status.api.serializers import StatusInlineUserSerializer

expire_delta = settings.JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']
jwt_payload_handler = settings.JWT_AUTH['JWT_PAYLOAD_HANDLER']
jwt_encode_handler = settings.JWT_AUTH['JWT_ENCODE_HANDLER']
jwt_repsonse_payload_handler = settings.JWT_AUTH['JWT_RESPONSE_PAYLOAD_HANDLER']
User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uri',
            'status'
        ]
    
    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse("api-user:detail", kwargs={"username": obj.username}, request=request)
    
    def get_status(self, obj):
        request = self.context.get('request')
        limit = 10
        if request:
            limit_query = request.GET.get('limit')
            try:
                limit = int(limit_query)
            except:
                pass
        qs = obj.status_set.all().order_by("-timestamp")
        data = {
            'uri': self.get_uri(obj=obj) + "status/",
            'last': StatusInlineUserSerializer(qs.first(), context={'request': request}).data,
            'recent': StatusInlineUserSerializer(qs[:limit], many=True, context={'request': request}).data
        }
        return data