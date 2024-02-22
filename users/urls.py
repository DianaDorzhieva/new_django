from django.urls import path
from users.apps import UsersConfig
from users.views import *
from rest_framework_simplejwt.views import (TokenRefreshView, TokenObtainPairView)

app_name = UsersConfig.name

urlpatterns = [
    path('client/create/', ClientCreateAPIView.as_view(), name='client_create'),
    path('client/', ClientListAPIView.as_view(), name='client_list'),
    path('client/<int:pk>/', ClientRetrieveAPIView.as_view(), name='client_pk'),
    path('client/update/<int:pk>/', ClientUpdateAPIView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDestroyAPIView.as_view(), name='client_delete'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
