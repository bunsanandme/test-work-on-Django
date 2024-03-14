from django.contrib.auth import authenticate
from rest_framework import serializers
from event_app.serializers import OrganizationSerializer

from .models import User

class UserSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(many=False)
    class Meta:
        model = User
        fields = ("id", "username", "email", "phone_number", "organization")

class UserRegisterationSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(many=False)
    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "phone_number", "organization")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
