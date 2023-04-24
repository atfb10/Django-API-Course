from django.contrib import admin

# Register your models here.
from .forms import StatusForm
from .models import Status

class StatusAdmin(admin.ModelAdmin):
    '''
    display how Status is viewed in the admin
    include form that cleans Status objects 
    '''
    list_display = ['user', '__str__']
    form = StatusForm

# Register models in admin
admin.site.register(Status, StatusAdmin)