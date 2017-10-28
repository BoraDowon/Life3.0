from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^articles', views.api_home_articles),
    url(r'^life-logs', views.api_life_logs),
]