# Generated by Django 5.0.1 on 2024-02-06 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название курса')),
                ('img', models.ImageField(upload_to='course/', verbose_name='превью')),
                ('text', models.TextField(verbose_name='описание')),
                ('materials', models.ManyToManyField(to='materials.materials', verbose_name='уроки')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
    ]
