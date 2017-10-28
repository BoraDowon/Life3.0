from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^life-logs', views.api_life_logs),
]
