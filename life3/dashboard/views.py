from django.http import JsonResponse, HttpRequest, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

import json

from . import services

from life3.dashboard.custom_middleware import auth_test
from django.utils.decorators import method_decorator

# TODO: TBD
# In a current url policy, url including overlaps between a render page and an api path.
# If we use a class for html rendering such as login, we should separate an app by a function based not a service based.


@auth_test
def api_home(request: HttpRequest):
    return render(request, 'home.html')


class LifeCardList(APIView):
    """
    List all lifecards.
    """
    @method_decorator(auth_test)
    def get(self, request: HttpRequest, format=None):
        lifecards = services.read_events()
        return Response({'events': lifecards})

    def post(self, request: HttpRequest, format=None):
        submitted_data: dict = json.loads(request.body)
        is_success = services.create_event(submitted_data)
        message = 'success' if is_success else 'fail'
        result_json = {'result': message}
        return Response(result_json)


class LifeCardDetail(APIView):
    def get(self, request: HttpRequest, card_pk, format=None):
        pass

    def post(self, request: HttpRequest, format=None):
        pass

    def put(self, request: HttpRequest, card_pk, format=None):
        pass

    def delete(self, request: HttpRequest, card_pk, format=None):
        pass

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
