# Generated by Django 5.0.1 on 2024-02-08 07:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_remove_course_materials'),
        ('materials', '0002_alter_materials_img_alter_materials_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='materials',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.course', verbose_name='курс'),
        ),
    ]
