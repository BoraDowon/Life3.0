from django.db import models


class LifeCard(models.Model):
    STATUS_INFO = (
        ('0', 'Active'),
        ('1', 'Inactive'),
    )

    TYPE_INFO = (
        ('W', 'Work'),
        ('P', 'Play'),
        ('R', 'Rest'),
    )

    title = models.CharField(max_length=500)
    timestamp = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_INFO)
    type = models.CharField(max_length=1, choices=TYPE_INFO)

    # account ID which is same as account_id in life3.user.models.LifeUser
    account_id = models.CharField(max_length=30, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'LifeCard Model : {}, {}, {}, {}'.\
            format(self.title, self.timestamp, self.type, self.status)

    class Meta:
        ordering = ['-timestamp']

'''
# TODO TBD: UserModel
from django.contrib.auth.models import AbstractBaseUser
from .managers import LifeUserManager


class LifeUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = LifeUserManager()
    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.email

    def get_full_name(self):
        pass

    def get_short_name(self):
        pass

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
'''
