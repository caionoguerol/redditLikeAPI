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
from comments import views as commentviews

from helpers.health_check_view import health_check

###
# URLs
###

router = routers.DefaultRouter()
router.register(r'login', userviews.LoginViewSet, basename='login')
router.register(r'users', userviews.UsersViewSet, basename='users')
router.register(r'topics', topicviews.TopicViewSet)

topics_router = routers.NestedSimpleRouter(router, r'topics', lookup='url_name')
topics_router.register(r'posts', postsviews.PostViewSet, basename='topic')

posts_router = routers.NestedSimpleRouter(topics_router, r'posts', lookup='post')
posts_router.register(r'comments', commentviews.CommentsViewSet, basename='post')
#
# router.register(r'posts', postsviews.PostViewSet, basename='posts')
# router.register(r'comments', commentviews.CommentsViewSet, basename='comments')
# router.register(r'topics', TopicsViewSet)

urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),
    # Applications
    url(r'', include(router.urls)),
    url(r'', include(topics_router.urls)),
    url(r'', include(posts_router.urls))

    # url(r'^', include('accounts.urls')),
    # url(r"userview/", views.UserListAPI.as_view()),
    # url(r"usercreate/", views.UserCreateAPI.as_view()),
    # url(r'(?P<id>\d+)/userupdate/$', views.UserUpdateAPI.as_view())
    # url(r'userupdate/', views.UserUpdateAPI.as_view())

]
