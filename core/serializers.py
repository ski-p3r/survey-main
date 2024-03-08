# serializers.py

from djoser.serializers import UserCreateSerializer
from .models import User
from rest_framework import serializers

class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'user_type'] 

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'name', 'email', 'password', 'phone', 'address', 'user_type', 'survey')

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
            phone=validated_data['phone'],
            address=validated_data['address'],
            user_type=validated_data['user_type']
        )
        return user
