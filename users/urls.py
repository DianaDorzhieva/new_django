from django.urls import path
from users.apps import UsersConfig
from users.views import PaymentCreateAPIView, PaymentListAPIView, PaymentRetrieveAPIView, \
    PaymentUpdateAPIView, PaymentDestroyAPIView, UserCreateAPIView, UserListAPIView, \
    UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView
from rest_framework_simplejwt.views import (TokenRefreshView, TokenObtainPairView)

app_name = UsersConfig.name

urlpatterns = [
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('payment/', PaymentListAPIView.as_view(), name='payment_list'),
    path('payment/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment_pk'),
    path('payment/update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='payment_update'),
    path('payment/delete/<int:pk>/', PaymentDestroyAPIView.as_view(), name='payment_delete'),

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
