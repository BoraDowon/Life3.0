from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

from . import services


def home(request):
    return render(request, 'home.html')


def home_articles(request):
    posts = []
    a1 = {'id': 1, 'title': 'test1'}
    a2 = {'id': 2, 'title': 'test2'}
    a3 = {'id': 3, 'title': 'test3'}

    posts.append(a1)
    posts.append(a2)
    posts.append(a3)

    posts_map = {'articles': posts}
    return JsonResponse(posts_map)


# TODO: modify HttpResponse to JsonResponse later
def get_life_logs(request):
    life_jsons = services.read_events()
    return HttpResponse(life_jsons, content_type='application/json')

