import inspect

from posts.models import Post
from posts.api.serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from topics.models import Topic
from users.api import permissions


class PostViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = PostSerializer
    permission_classes = (permissions.OwnerUpdate, IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        queryset = Topic.objects.filter(url_name=self.kwargs['topic_url_name']).values('id')
        topic_pk = (queryset[0]).get('id')
        return Post.objects.filter(topic=topic_pk)

    def perform_create(self, serializer):
        query_id = Topic.objects.filter(url_name=self.kwargs['topic_url_name']).values('id')
        serializer.save(author=self.request.user, topic_id=(query_id[0]).get('id'))
