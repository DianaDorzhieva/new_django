from rest_framework import generics
from users.models import Client
from users.serliazers import ClientSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import  OrderingFilter


class ClientCreateAPIView(generics.CreateAPIView):
    serializer_class = ClientSerializer


class ClientListAPIView(generics.ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('materials', 'method_pay')
    ordering_fields = ('day_pay',)


class ClientRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientDestroyAPIView(generics.DestroyAPIView):
    queryset = Client.objects.all()

