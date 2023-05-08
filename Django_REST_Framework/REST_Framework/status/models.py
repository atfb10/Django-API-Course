from django.conf import settings
from django.db import models

def upload_status_image(instance, filnename):
    '''
    string of url for images to be uploaded to
    '''
    return f'status/{instance.user}/{filnename}'

class StatusQueryset(models.QuerySet):
    pass

class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQueryset(self.model, using=self._db)

# fb status, insta post, tweet, etc
class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_status_image, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    objects = StatusManager().get_queryset()

    def __repr__(self) -> str:
        '''
        repr method will return user + first 50 characters of their content
        '''
        return f'{self.content[:50]}'
    
    def __str__(self) -> str:
        '''
        str method will return user + first 50 characters of their content
        '''
        return f'{self.content[:50]}...'
    
    class Meta:
        verbose_name = 'Status Post'
        verbose_name_plural = 'Status Posts'