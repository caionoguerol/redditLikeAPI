from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True, default = 'n/a')

    # USERNAME_FIELD =
    REQUIRED_FIELDS = ['email', 'password']

#     def __str__(self):
#         return "{}".format(self.email)
#
# class UserProfile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')