from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^lifecards/$', views.LifeCardList.as_view()),
    url(r'^lifecards/(?P<card_pk>[0-9]+)/$', views.LifeCardDetail.as_view()),

    url(r'^stats/', views.api_statistics),
]
