from django.http import JsonResponse, HttpRequest, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response

import json

from . import services


# TODO: remove
def api_home(request: HttpRequest):
    code = request.GET.get('code')
    print('Facebook Token: ' + code)
    '''
    url = 'https://graph.facebook.com/me?access_token={}&fields=id.name,email,picture'
    '''
    return render(request, 'home.html')


def facebook_oauth_test(request: HttpRequest):
    client_id = '742227722635556'

    url = 'https://www.facebook.com/v2.10/dialog/oauth?client_id={}&redirect_uri=http://localhost:8000/'.format(client_id)
    return HttpResponseRedirect(url)


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
