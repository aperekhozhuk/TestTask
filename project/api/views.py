from django.contrib.auth.models import User
from api.serializers import SignUpSerializer
from rest_framework import generics


class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
