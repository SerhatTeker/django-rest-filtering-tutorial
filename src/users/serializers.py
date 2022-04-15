from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "name",
            "email",
        )
        read_only_fields = ("username",)


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "auth_token",
        )
        read_only_fields = ("auth_token",)
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        return User.objects.create_user(**validated_data)
