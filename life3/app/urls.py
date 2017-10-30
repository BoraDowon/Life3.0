from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^lifecards/$', views.LifeCardList.as_view()),
    #url(r'^lifecards/(?P<pk>[0-9]+)/$', views.LifeCardDetail.as_view()),
    #url(r'^lifecards', views.api_lifecards),
    url(r'^stats', views.api_statistics),
]
