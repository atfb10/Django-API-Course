from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import generics, permissions
import datetime
from rest_framework.reverse import reverse as api_reverse
from django.utils import timezone

expire_delta = settings.JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']
jwt_payload_handler = settings.JWT_AUTH['JWT_PAYLOAD_HANDLER']
jwt_encode_handler = settings.JWT_AUTH['JWT_ENCODE_HANDLER']
jwt_repsonse_payload_handler = settings.JWT_AUTH['JWT_RESPONSE_PAYLOAD_HANDLER']
User = get_user_model()

class UserPublicSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uri'
        ]
    
    def get_uri(self, obj):
        return api_reverse('api-status:detail', kwargs={"id": obj.id}, request=self.context.get('request'))

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})
    token = serializers.SerializerMethodField(read_only=True)
    expires = serializers.SerializerMethodField(read_only=True)
    message = serializers.SerializerMethodField(read_only=True)
    class Meta:
        fields = [
            'username',
            'email',
            'password',
            'password',
            'token',
            'expires',
            'message'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def get_message(self,obj):
        return "thank you for registering. please verify email"

    def get_expires(self, obj):
        return timezone.now() + expire_delta - datetime.timedelta(seconds=200)

    def get_token(self, obj): # instance of the model
        user = obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        context = self.context
        response = jwt_repsonse_payload_handler(token, user, request=context['request'])
        return response

    def validate_email(self, value):
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError('User with this email already exists')
        return value
    
    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError('User with this username already exists')
        return value
    
    def validate(self, data):
        pw = data.get('password')
        pw2 = data.pop('password2')
        if pw != pw2:
            raise serializers.ValidationError('Passwords must match')
        return data
    
    def create(self, validated_data):
        user_obj = User(username=validated_data.get('username'), email=validated_data.get('email'))
        user_obj.set_password(validated_data.get('password'))
        user_obj.is_active = False
        user_obj.save()
        return user_obj