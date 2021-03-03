from posts.models import Post
from posts.api.serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from users.api import permissions
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, )
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (permissions.OwnerUpdate,IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)





