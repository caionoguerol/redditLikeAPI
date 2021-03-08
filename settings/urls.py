"""
backend-challenge-001 URL Configuration
"""
###
# Libraries
###
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_nested import routers
from users import views as userviews
from topics import views as topicviews
from posts import views as postsviews
from comments import views as commentviews



###
# URLs
###

router = routers.DefaultRouter()
router.register(r'login', userviews.LoginViewSet, basename='login')
router.register(r'users', userviews.UsersViewSet, basename='users')
router.register(r'topics', topicviews.TopicViewSet, basename='topics')


topics_router = routers.NestedSimpleRouter(router, r'topics', lookup='topic')
topics_router.register(r'posts', postsviews.PostViewSet, basename='topic')

posts_router = routers.NestedSimpleRouter(topics_router, r'posts', lookup='post')
posts_router.register(r'comments', commentviews.CommentsViewSet, basename='post')


urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),
    # Applications
    url(r'', include(router.urls)),
    url(r'', include(topics_router.urls)),
    url(r'', include(posts_router.urls))


]
