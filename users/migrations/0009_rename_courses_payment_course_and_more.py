# Generated by Django 5.0.2 on 2024-03-08 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_rename_client_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='courses',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='materials',
            new_name='material',
        ),
    ]
