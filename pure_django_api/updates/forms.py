from django import forms

from .models import Update as UpdateModel

class UpdateModelForm(forms.ModelForm):
    class Meta:
        model = UpdateModel
        fields = [
            'user',
            'content',
            'image'
        ]
    
    def clean(self, *args, **kwargs):
        '''
        ensure there is either content or image
        '''
        data = self.cleaned_data
        content = data.get('content', None)
        if content == None:
            content = None
        if img == 'no image':
            img = None
        img = data.get('image', None)
        if content is None and img is None:
            raise forms.ValidationError('Content or Image is required')
        return super().clean(*args, **kwargs)