from rest_framework.generics import RetrieveAPIView, CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from users.models import User, Location
from users.serializers import UserSerializer, UserListSerializer, UserDetailSerialize, LocationSerializer, \
    UserCreateSerializer


class UserPagination(PageNumberPagination):
    page_size = 4


class UserListView(ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    pagination_class = UserPagination


class UserDetailView(RetrieveAPIView):
    serializer_class = UserDetailSerialize
    queryset = User.objects.all()


class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class UserUpdateView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDeleteView(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LocationViewSet(ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
