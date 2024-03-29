# Generated by Django 5.0.2 on 2024-03-09 06:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_course_price'),
        ('materials', '0006_materials_owner'),
        ('users', '0009_rename_courses_payment_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course', verbose_name='курсы'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.materials', verbose_name='уроки'),
        ),
    ]
