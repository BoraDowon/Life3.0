from django.shortcuts import render
from django.http import JsonResponse, HttpRequest

import json

from . import services


# TODO: remove
def api_home(request):
    return render(request, 'home.html')


def api_life_logs(request: HttpRequest) -> JsonResponse:
    """ API for life logs

    :param request: http request
    :return: JSON response
    """
    if request.method == 'POST':
        submitted_data: dict = json.loads(request.body)
        is_success = services.create_event(submitted_data)
        message = 'success' if is_success else 'fail'
        return JsonResponse({'result': message})

    elif request.method == 'GET':
        life_logs = services.read_events()
        return JsonResponse({'events': life_logs})

    else:
        return JsonResponse({'result': f'Unsupported method {request.method}'})


