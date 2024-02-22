from rest_framework import serializers
from materials.models import Materials
from rest_framework.relations import SlugRelatedField
from course.models import Course
from users.models import User


class MaterialsSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field='name', queryset=Course.objects.all())
    owner = SlugRelatedField(slug_field='email', queryset=User.objects.all())
    class Meta:
        model = Materials
        fields = '__all__'
