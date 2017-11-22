from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from functools import wraps

class SimpleMiddlerware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        '''
        if request.path == '/login/' or request.path == '/':
            print('no auth')
        else:
            status = self.process_request(request)
            if status == 'Fail':
                return JsonResponse(({'detail': 'Authentication credentials were not provided.'}), status=403)
        '''
        return self.get_response(request)

    def process_request(self, request: HttpRequest):
        try:
            access_token = request.META.get('HTTP_AUTHORIZATION').replace('TOKEN ', '')
            if access_token == '1234':
                return 'Success'
            else:
                return 'Fail'
        except AttributeError:
            return 'Fail'

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('process_view: ', request, view_args, view_func, view_kwargs)
        response = None
        return response

    def process_response(self, request, response):
        print('process_response: ', request.path)
        return response
