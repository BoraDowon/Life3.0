from django.conf.urls import url

from . import views

urlpatterns = [

    # login web
    url(r'^$', views.LoginHome.as_view()),

    # login authentication
    url(r'^api/auth/', views.LoginApi.as_view()),

]
