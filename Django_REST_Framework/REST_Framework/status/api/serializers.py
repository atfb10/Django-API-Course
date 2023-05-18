from rest_framework import serializers
from status.models import Status
from accounts.api.serializers import UserPublicSerializer

# NOTE: THIS IS JUST AN EXAMPLE OF CREATING A CUSTOM SERIALIZER that is not using a model. 
class CustomerSerializer(serializers.Serializer):
    content = serializers.CharField()
    email = serializers.EmailField()
    
class StatusSerializer(serializers.ModelSerializer):
    '''
    turn data into JSON and validate data
    '''
    user = UserPublicSerializer(read_only=True)
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image'
        ]
        read_only_fields = [
            'user'
        ]
    '''
    field level validation
    NOTE: just need to name validate_<fieldname>
    '''
    def validate_content(self, value):
        if len(value) > 10000:
            raise serializers.ValidationError("Content is wayyyy too long")
        return value
    
    '''
    entire data validation
    '''
    def validate(self, data):
        content = data.get('content', None)
        if content == "":
            content = None
        img = data.get('image', None)
        if content == None and img == None:
            raise serializers.ValidationError("Content OR image must be present!")
        return data