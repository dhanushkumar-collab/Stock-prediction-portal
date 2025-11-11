from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Stock  # optional; remove if you don't use Stock model yet

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, required=True)
    password2 = serializers.CharField(write_only=True, required=True, label="Confirm password")

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "password2")
        read_only_fields = ("id",)

    def validate(self, data):
        if data.get("password") != data.get("password2"):
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop("password2", None)
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

