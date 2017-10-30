from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json

from . import services


# TODO: remove
def api_home(request):
    return render(request, 'home.html')


class LifeCardList(APIView):
    """
    List all lifecards.
    """
    def get(self, request: HttpRequest, format=None):
        lifecards = services.read_events()
        return Response({'events': lifecards})

    def post(self, request: HttpRequest, format=None):
        submitted_data: dict = json.loads(request.body)
        is_success = services.create_event(submitted_data)
        message = 'success' if is_success else 'fail'
        return Response({'result': message})

@csrf_exempt
def api_lifecards(request: HttpRequest) -> JsonResponse:
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
        lifecards = services.read_events()
        return JsonResponse({'events': lifecards})

    else:
        return JsonResponse({'result': f'Unsupported method {request.method}'})


def api_statistics(request: HttpRequest) -> JsonResponse:
    if request.method == 'GET':
        lifestats = services.read_statistics()
        return JsonResponse({'statistics': lifestats})
    else:
        return JsonResponse({'statistics': f'Unsupported method {request.method}'})
