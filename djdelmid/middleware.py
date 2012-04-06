class DjangoDeleteMiddleware(object):
    def process_request(self, request):
        if request.POST.get('_method') == 'DELETE':
            request.method = 'DELETE'
