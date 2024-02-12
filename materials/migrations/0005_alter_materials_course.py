# Generated by Django 5.0.1 on 2024-02-12 10:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_remove_course_materials'),
        ('materials', '0004_alter_materials_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materials',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='course.course', verbose_name='курс'),
        ),
    ]
