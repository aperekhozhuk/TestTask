from django.contrib.auth.models import User
from api.models import Post, Like
from api.serializers import (
    SignUpSerializer,
    PostListSerializer,
    PostDetailSerializer,
    PostCreateSerializer,
)
from rest_framework import generics, mixins, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer


class PostViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return PostListSerializer
        elif self.action == "retrieve":
            return PostDetailSerializer
        else:
            return PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get_post_or_404_response(post_id):
        # Checking if Post exists:
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response(
                {"error": "Post Not Found"}, status=status.HTTP_404_NOT_FOUND
            )
        return post

    def post(self, request, post_id, format=None):
        post = self.get_post_or_404_response(post_id)
        if isinstance(post, Response):
            return post
        # Trying to put like:
        try:
            Like.objects.create(post=post, user=request.user)
        except IntegrityError:
            return Response(
                {"error": "You already liked this post!"},
                status=status.HTTP_403_FORBIDDEN,
            )
        return Response({"message": "Post liked!"}, status=status.HTTP_201_CREATED)

    def delete(self, request, post_id, format=None):
        post = self.get_post_or_404_response(post_id)
        if isinstance(post, Response):
            return post
        # Checking if user liked this post before
        try:
            like = Like.objects.get(post=post, user=request.user)
        except Like.DoesNotExist:
            return Response(
                {"error": "You didn't like this post!"},
                status=status.HTTP_403_FORBIDDEN,
            )
        like.delete()
        return Response({"message": "Post unliked!"}, status=status.HTTP_200_OK)
