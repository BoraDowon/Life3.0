from django.db import models


class LifeUser(models.Model):
    """
    Simple life user model
    """
    profile_name = models.TextField(max_length=50)
    profile_image_url = models.TextField(max_length=255)
    profile_email = models.EmailField(max_length=255, unique=True)
    account_type = models.TextField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f'name: {self.profile_name}, account_type: {self.account_type}, ' \
               f'email: {self.email}, active: {self.is_active}'
