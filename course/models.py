from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='название курса')
    img = models.ImageField(verbose_name='превью', upload_to='course/', **NULLABLE)
    text = models.TextField(verbose_name='описание')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
