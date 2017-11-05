from django.db import models


class LifeUser(models.Model):
    """
    Simple life user model for OAuth login
    """

    # user id from OAUTH
    account_id = models.TextField(max_length=30)

    # user token from OAUTH
    account_token = models.TextField(max_length=200)

    # user name from OAUTH
    profile_name = models.TextField(max_length=50)

    # e-mail address
    profile_email = models.EmailField(max_length=255)

    # user picture from OAUTH
    profile_image_url = models.TextField(max_length=255)

    # 'FACEBOOK' or 'KAKAO'
    account_type = models.TextField(max_length=10)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f'name: {self.profile_name}, account_type: {self.account_type}, ' \
               f'email: {self.email}, active: {self.is_active}'
