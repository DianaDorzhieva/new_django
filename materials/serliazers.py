from rest_framework import serializers
from materials.models import Materials

class MaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = '__all__'
