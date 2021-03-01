"""
backend-challenge-001 URL Configuration
"""
###
# Libraries
###
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework_nested import routers
from users import views



from helpers.health_check_view import health_check

###
# URLs
###

router = routers.DefaultRouter()
router.register(r'users', views.UsersViewSet, basename='Users')



#router.register(r'topics', TopicsViewSet)

urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Health Check
    url(r'health-check/$', health_check, name='health_check'),

    # Applications

    url(r'',include(router.urls)),

    # url(r'^', include('accounts.urls')),
    # url(r"userview/", views.UserListAPI.as_view()),
    # url(r"usercreate/", views.UserCreateAPI.as_view()),
    # url(r'(?P<id>\d+)/userupdate/$', views.UserUpdateAPI.as_view())
    # url(r'userupdate/', views.UserUpdateAPI.as_view())

    ]