from rest_framework import serializers

from users.models import users as user_models


class UserSignUpSerializer(serializers.Serializer):
    key = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    name = serializers.CharField()
    nickname = serializers.CharField()


class UserSignInSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    phone_number = serializers.CharField(required=False)
    password = serializers.CharField()


class UserTokenSerializer(serializers.Serializer):
    token = serializers.CharField()


class ResetPasswordSerializer(serializers.Serializer):
    key = serializers.CharField()
    password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.User
        fields = ["email", "name", "nickname", "created_at", "last_login"]
