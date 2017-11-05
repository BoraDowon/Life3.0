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

        message = 'success'
        # userId, userName, accessToken, type
        if profile['userId']:
            if UserService.is_valid_user(profile['userId']):
                UserService.update_user_profile(profile)
            else:
                UserService.create_user_profile(profile)
        else:
            message = 'userId is empty!'

        return Response({'result', message})

    def get(self):
        return Response({'result', 'unsupported request'})
