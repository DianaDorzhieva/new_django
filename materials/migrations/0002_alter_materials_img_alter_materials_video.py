# Generated by Django 5.0.1 on 2024-02-07 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materials',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='course/', verbose_name='превью'),
        ),
        migrations.AlterField(
            model_name='materials',
            name='video',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ссылка на видео'),
        ),
    ]
