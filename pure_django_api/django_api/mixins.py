from django.http import JsonResponse, HttpResponse

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
    
class HttpResponseMixin(object):
    is_json = False

    def render_to_response(self, data, status=200):
        content_type = 'text/html'
        if self.is_json:
            content_type = 'application/json'
        return HttpResponse(data, content_type=content_type, status=status)
