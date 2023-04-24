from rest_framework import serializers
from status.models import Status

class StatusSerializer(serializers.ModelSerializer):
    '''
    turn data into JSON and validate data
    '''
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image'
        ]