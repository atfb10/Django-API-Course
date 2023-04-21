from django.conf import settings
from django.core.serializers import serialize
from django.db import models

def upload_update_image(instance, filename):
    return f'updates/{instance.user}{filename}'

class UpdateQuerySet(models.QuerySet):
    def serialize(self):
        qs = self
        return serialize('json', qs, fields=('user', 'content', 'image'))
    
class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)

# Create your models here.
class Update(models.Model):
    '''
    model to use as example
    '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    objects = UpdateManager()

    def __str__(self) -> str:
        return self.content or ""
    
    def serialize(self):
        '''
        create a serializer as method of class
        '''
        return serialize(format='json', queryset=[self], fields=('user', 'content', 'image'))