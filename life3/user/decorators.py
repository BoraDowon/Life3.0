from django.http import HttpRequest
from django.http import JsonResponse
from functools import wraps


def _auth_test_helper(request: HttpRequest):
    try:
        access_token = request.META.get('HTTP_AUTHORIZATION').replace('TOKEN ', '')
        if access_token == '1234':
            return True
        else:
            return False
    except AttributeError:
        return False


def auth_test(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        result = _auth_test_helper(request)
        print(result)
        if result is not False:
            return func(request, *args, **kwargs)
        else:
            return JsonResponse(({'detail': 'Authentication credentials were not provided.'}), status=403)
    return inner
