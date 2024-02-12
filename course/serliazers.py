from rest_framework import serializers
from materials.serliazers import MaterialsSerializer
from course.models import Course


class CourseSerializer(serializers.ModelSerializer):
    count_materials = serializers.SerializerMethodField()
    materials = MaterialsSerializer(many=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_count_materials(self, instance):
        return instance.materials.count()
