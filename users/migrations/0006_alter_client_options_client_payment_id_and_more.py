# Generated by Django 5.0.2 on 2024-03-05 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_client_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Информация о платеже пользователя', 'verbose_name_plural': 'Информация о платежах пользователя'},
        ),
        migrations.AddField(
            model_name='client',
            name='payment_id',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='id  оплаты'),
        ),
        migrations.AddField(
            model_name='client',
            name='payment_url',
            field=models.URLField(blank=True, null=True, verbose_name='ссылка для оплаты'),
        ),
    ]
