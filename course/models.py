from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='название курса')
    img = models.ImageField(verbose_name='превью', upload_to='course/', **NULLABLE)
    text = models.TextField(verbose_name='описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)
    price = models.PositiveIntegerField(default=100, verbose_name='цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Subscriptions(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             verbose_name='пользователь', related_name='user')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    is_activate = models.BooleanField(default=True, verbose_name='активация подписки')

    def __str__(self):
        return f"{self.user} {self.course}"

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
