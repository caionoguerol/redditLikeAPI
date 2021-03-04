from comments.models import Comment
from comments.api.serializers import CommentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from users.api import permissions



class CommentsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, )
    serializer_class = CommentSerializer
    # queryset = Comment.objects.all()
    permission_classes = (permissions.OwnerUpdate,IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs['post_pk'])

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)