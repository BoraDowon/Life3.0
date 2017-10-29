from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^lifecards', views.api_lifecards),
    url(r'^stats', views.api_statistics),
]
