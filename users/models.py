from django.db import models
from django.contrib.auth.models import AbstractUser
NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    DoesNotExist = None
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    FIO = models.CharField(max_length=300, verbose_name='ФИО',  **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=50, verbose_name='телефон')
    county = models.CharField(max_length=50, verbose_name='город')


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


