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
from users import views as userviews
from topics import views as topicviews
from posts import views as postsviews

from helpers.health_check_view import health_check

###
# URLs
###

router = routers.DefaultRouter()
router.register(r'users', userviews.UsersViewSet, basename='Users')
router.register(r'topics', topicviews.TopicViewSet, basename='Topics')
router.register(r'posts', postsviews.PostViewSet, basename='Posts')

# router.register(r'topics', TopicsViewSet)

urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Health Check
    url(r'health-check/$', health_check, name='health_check'),

    # Applications

    url(r'', include(router.urls)),
    # url(r'', include(router_topics.urls))

    # url(r'^', include('accounts.urls')),
    # url(r"userview/", views.UserListAPI.as_view()),
    # url(r"usercreate/", views.UserCreateAPI.as_view()),
    # url(r'(?P<id>\d+)/userupdate/$', views.UserUpdateAPI.as_view())
    # url(r'userupdate/', views.UserUpdateAPI.as_view())

]
