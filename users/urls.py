from django.urls import path
from users.apps import UsersConfig
from users.views import ClientCreateAPIView, ClientListAPIView, ClientRetrieveAPIView, \
    ClientUpdateAPIView, ClientDestroyAPIView, UserCreateAPIView, UserListAPIView, \
    UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView
from rest_framework_simplejwt.views import (TokenRefreshView, TokenObtainPairView)

app_name = UsersConfig.name

urlpatterns = [
    path('client/create/', ClientCreateAPIView.as_view(), name='client_create'),
    path('client/', ClientListAPIView.as_view(), name='client_list'),
    path('client/<int:pk>/', ClientRetrieveAPIView.as_view(), name='client_pk'),
    path('client/update/<int:pk>/', ClientUpdateAPIView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDestroyAPIView.as_view(), name='client_delete'),

    # путь для токена
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # путь для пользователя
    path('user/create/', UserCreateAPIView.as_view(), name='user_create'),
    path('user/', UserListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_pk'),
    path('user/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),

]
