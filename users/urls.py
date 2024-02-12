from django.urls import path
from users.apps import UsersConfig
from users.views import *

app_name = UsersConfig.name

urlpatterns = [
    path('client/create/', ClientCreateAPIView.as_view(), name='client_create'),
    path('client/', ClientListAPIView.as_view(), name='client_list'),
    path('client/<int:pk>/', ClientRetrieveAPIView.as_view(), name='client_pk'),
    path('client/update/<int:pk>/', ClientUpdateAPIView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDestroyAPIView.as_view(), name='client_delete'),

]
