from django.http import HttpRequest
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from life3.user.user_service import UserService


class LoginHome(TemplateView):
    """
    Login template
    """
    template_name = 'login.html'


class LoginApi(APIView):

    def post(self, request: HttpRequest):
        """
        Create user from profile based on OAuth.
        If user already exists or token has expired, update user from profile

        :param request: HttpRequest
        :return: JSON response
        """

        profile: dict = json.loads(request.body)
        user_service = UserService()

        message = 'success'
        if profile['accessToken']:
            if user_service.is_valid_user(profile['accessToken']):
                user_service.update_user_profile(profile)
            else:
                user_service.create_user_profile(profile)
        else:
            message = 'token is not included!'

        return Response({'result', message})

    def get(self):
        return Response({'result', 'unsupported request'})
