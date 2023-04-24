from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from status.api.serializers import StatusSerializer
from status.models import Status

'''
NOTE TO ME!
This all needs to run in the python shell. CANNOT just run the script.
I have written it here, just so I do not have to continuously rewrite it in the shell
'''

# Retrieve & serialize single object
obj = Status.objects.first()
serializer = StatusSerializer(obj)
json_data = JSONRenderer().render(serializer.data)
print(json_data)

# Retrieve & Serialize a queryset
qs = Status.objects.all()
serializer = StatusSerializer(qs, many=True)
json_data = JSONRenderer().render(serializer.data)
print(json_data)

# Create object
data = {
    'user': 1,
    'content': 'I am content created using Django REST Framework'
}
serializer = StatusSerializer(data=data)
serializer.is_valid() # Checks if data is valid -> this will return True in this instance. NOTE: MUST call is_valid before saving
serializer.save() # Now run the retrieve and serialize on last Status object

# Update object
obj = Status.objects.last()
data = {'user': 1, 'content': 'Updated Content!'}
serializer = StatusSerializer(obj, data=data)
serializer.is_valid()
serializer.save()

# Delete Object (Creating then immediately deleting)
data_to_delete = {
    'user': 1,
    'content': 'delete me'
}
serializer = StatusSerializer(obj, data=data_to_delete)
serializer.is_valid()
create_obj = serializer.save() # .save() returns an instance of the object!

obj = Status.objects.last()
obj.delete()