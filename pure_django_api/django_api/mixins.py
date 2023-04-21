from django.http import JsonResponse

class JsonResponseMixin(object):
    '''
    create mixin class so I don't have to update data format or call JsonResponse 
    '''
    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(self.get_data(context=context), **response_kwargs)
    
    def get_data(self, context):
        '''
        update data if needed
        '''
        return context