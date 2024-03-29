from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from course.models import Course
from materials.models import Materials

NULLABLE = {'blank': True, 'null': True}


class UserRole(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    DoesNotExist = None
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    FIO = models.CharField(max_length=300, verbose_name='ФИО', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=50, verbose_name='телефон', **NULLABLE)
    county = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    role = models.CharField(max_length=50, choices=UserRole.choices, default=UserRole.MEMBER)
    is_active = models.BooleanField(default=True)



    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payment(models.Model):
    method_pay_choices = [('cash', 'наличными'), ('card', 'картой')]

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='пользователь',
                             **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE,
                                   verbose_name='курсы')
    material = models.ForeignKey(Materials, on_delete=models.CASCADE, **NULLABLE,
                                     verbose_name='уроки')
    day_pay = models.DateField(verbose_name='дата оплаты', **NULLABLE)
    method_pay = models.TextField(choices=method_pay_choices,
                                  verbose_name='метод оплаты', **NULLABLE)
    money = models.IntegerField(verbose_name='сумма оплаты', **NULLABLE)

    payment_url = models.TextField(verbose_name='ссылка для оплаты', **NULLABLE)


    def __str__(self):
        return f'{self.user} оплатил курс {self.courses}, cумма {self.money}'

    class Meta:
        verbose_name = 'Информация о платеже пользователя'
        verbose_name_plural = 'Информация о платежах пользователя'
