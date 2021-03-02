from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class UserProfileManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Users must have an username.')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True

        user.save()

        return


class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    # name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    # username = models.CharField(max_length=15, unique=True, default = 'n/a')

    # USERNAME_FIELD =
    # REQUIRED_FIELDS = ['email', 'password']

#     def __str__(self):
#         return "{}".format(self.email)
#
# class UserProfile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
