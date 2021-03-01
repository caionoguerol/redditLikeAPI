from users.models import User
from rest_framework import generics
from users.api.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


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
    serializer_class = UserSerializer
    queryset = User.objects.all()


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


