from django.db import models
from config import settings
from course.models import Course

NULLABLE = {'blank': True, 'null': True}


class Materials(models.Model):
    name = models.CharField(max_length=100, verbose_name='название урока')
    img = models.ImageField(verbose_name='превью', upload_to='course/', **NULLABLE)
    text = models.TextField(verbose_name='описание')
    video = models.CharField(max_length=100, verbose_name='ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE,
                               related_name='materials')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
