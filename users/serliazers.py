from rest_framework import serializers

from course.serliazers import SubscriptionSerializer
from users.models import Client, User


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserListSerializer(serializers.ModelSerializer):
    active = serializers.SerializerMethodField()

    class Meta:
        model = User
        #fields = ('email', 'FIO', 'phone', 'county', 'active')
        fields = '__all__'

    def get_active(self, instance):
        return instance.is_active
