from django.contrib import admin

# Register your models here.
from .models import Update as UpdateModel

admin.site.register(UpdateModel)