from rest_framework import generics
from users.models import Client, User
from users.permission import IsUser
from users.serliazers import ClientSerializer, UserSerializer, UserListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

""" Контроллеры для клиента"""


class ClientCreateAPIView(generics.CreateAPIView):
    serializer_class = ClientSerializer


class ClientListAPIView(generics.ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('materials', 'method_pay')
    ordering_fields = ('day_pay',)
    permission_classes = [IsAuthenticated]


class ClientRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = [IsAuthenticated]


class ClientUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = [IsAuthenticated]


class ClientDestroyAPIView(generics.DestroyAPIView):
    queryset = Client.objects.all()
    permission_classes = [IsAuthenticated]


""" Контроллеры для пользователя"""


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    #permission_classes = [IsAuthenticated]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsUser]


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsUser]
