from users.models import User
from users.api.serializers import UserSerializer
from rest_framework import viewsets


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


