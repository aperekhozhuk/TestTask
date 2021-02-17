from django.contrib.auth.models import User
from api.models import Post
from api.serializers import (
    SignUpSerializer,
    PostListSerializer,
    PostDetailSerializer,
    PostCreateSerializer,
)
from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly


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
