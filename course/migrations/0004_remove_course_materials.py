# Generated by Django 5.0.1 on 2024-02-08 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_course_materials'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='materials',
        ),
    ]
