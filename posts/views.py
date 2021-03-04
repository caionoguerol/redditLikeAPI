from posts.models import Post
from posts.api.serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from users.api import permissions



class PostViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, )
    serializer_class = PostSerializer
    # queryset = Post.objects.all()
    permission_classes = (permissions.OwnerUpdate,IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        return Post.objects.filter(topic=self.kwargs['topic_pk'])

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)





