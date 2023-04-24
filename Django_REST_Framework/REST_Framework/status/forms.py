from django import forms

from .models import Status

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['user', 'content', 'image']

    def clean(self, *args, **kwargs):
        '''
        call cleaning functions
        '''
        self.ensure_content()
        self.content_limit()
        return
    
    def ensure_content(self, *args, **kwargs):
        '''
        ensure that there is either content OR an image
        '''
        data = self.cleaned_data
        content = data.get('content', None)
        img = data.get('image', None)
        if content == '':
            content = None
        if img == '':
            img = None
        if content is None and img is None:
            raise forms.ValidationError('Content OR image is required')

        return super().clean(*args, **kwargs) 
    
    def content_limit(self, *args, **kwargs):
        '''
        set 240 character limit
        '''
        content = self.cleaned_data.get('content')
        if len(content) > 240:
            raise forms.ValidationError('Content must be less than 240 characters')
        return content