import secrets

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import uuid

class User(AbstractUser):
    id = models.CharField(
        max_length=11,
        unique=True,
        primary_key=True,
        blank=True,
    )

    username = models.CharField(blank=True, null=True, max_length=50)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['email', 'username']

    def __str__(self):
        return "{}".format(self.email)

    # def save(self, *args, **kwargs):
    #     id = secrets.token_urlsafe(8)
    #     while User.objects.filter(id=id).count() != 0:
    #         id = secrets.token_urlsafe(8)
    #     self.id = id
    #     super(User, self).save(*args, **kwargs)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    title = models.CharField(max_length=5)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=5)