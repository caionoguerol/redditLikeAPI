from topics.models import Topic
from topics.api.serializers import TopicSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from users.api import permissions


class TopicViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
    permission_classes = (permissions.OwnerUpdate, IsAuthenticatedOrReadOnly)
    lookup_field = 'url_name'
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
