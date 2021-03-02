from users.api.permissions import UpdateOwnProfile
from users.models import UserProfile
from rest_framework import generics
from users.api.serializers import UserProfileSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from users.api import permissions

# class UserList(APIView):
#
#     def get(self,request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
#     def post(self):
#         pass
#

class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

class LoginViewSet(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        return ObtainAuthToken().post(request)

# class UserListAPI(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# #
# class UserCreateAPI(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserUpdateAPI(generics.UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = 'id'
#
