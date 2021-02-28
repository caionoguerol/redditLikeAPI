"""
backend-challenge-001 URL Configuration
"""
###
# Libraries
###
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from users.views import UsersViewSet
from helpers.health_check_view import health_check

###
# URLs
###

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)


urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Health Check
    url(r'health-check/$', health_check, name='health_check'),
    # Applications
   # url(r'^', include('accounts.urls')),
    url(r'',include(router.urls))
]
