from django.conf import settings
from django.db import models

def upload_update_image(instance, filename):
    return f'updates/{instance.user}{filename}'

# Create your models here.
class Update(models.Model):
    '''
    update content model
    '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.content or ""