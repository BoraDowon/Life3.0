from django.shortcuts import render
from django.http import JsonResponse, HttpRequest

from . import services


def api_home(request):
    return render(request, 'home.html')


def api_home_articles(request):
    posts = []
    a1 = {'id': 1, 'title': 'test1'}
    a2 = {'id': 2, 'title': 'test2'}
    a3 = {'id': 3, 'title': 'test3'}

    posts.append(a1)
    posts.append(a2)
    posts.append(a3)

    posts_map = {'articles': posts}
    return JsonResponse(posts_map)


def api_get_life_logs(request: HttpRequest) -> JsonResponse:
    """ API for getting life logs

    :param request: http request
    :return: JSON response
    """
    life_logs = services.read_events()
    return JsonResponse({'events': life_logs})

