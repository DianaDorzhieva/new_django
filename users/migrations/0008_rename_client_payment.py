# Generated by Django 5.0.2 on 2024-03-08 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_course_price'),
        ('materials', '0006_materials_owner'),
        ('users', '0007_remove_client_payment_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Client',
            new_name='Payment',
        ),
    ]
