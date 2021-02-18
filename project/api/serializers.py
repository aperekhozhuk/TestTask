from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from api.models import Post


class UserProfileSerializer(serializers.ModelSerializer):
    last_login = serializers.ReadOnlyField(source="profile.last_login")
    last_request = serializers.ReadOnlyField(source="profile.last_request")

    class Meta:
        model = User
        fields = ("id", "username", "last_login", "last_request")


class SignUpSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={"input_type": "password"},
    )

    class Meta:
        model = User
        fields = ("id", "username", "password")

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"], password=validated_data["password"]
        )
        return user


class PostGeneralSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source="user.id")


class PostListSerializer(PostGeneralSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "text", "user_id")
        extra_kwargs = {"text": {"write_only": True}}


class PostDetailSerializer(PostGeneralSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "text", "user_id")


class PostCreateSerializer(PostGeneralSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "text", "user_id")
        extra_kwargs = {"title": {"write_only": True}, "text": {"write_only": True}}
