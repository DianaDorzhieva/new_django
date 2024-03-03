from rest_framework import serializers
from materials.serliazers import MaterialsSerializer
from course.models import Course, Subscriptions


class CourseSerializer(serializers.ModelSerializer):
    count_materials = serializers.SerializerMethodField(read_only=True)
    materials = MaterialsSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_count_materials(self, instance):
        return instance.materials.count()


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = '__all__'
