from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ExcelData

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ExcelDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelData
        fields = ['id', 'user', 'title', 'description', 'location', 'date', 'uploaded_at']
        read_only_fields = ['user', 'uploaded_at']
