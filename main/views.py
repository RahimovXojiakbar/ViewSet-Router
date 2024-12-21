from django.shortcuts import render
from . import models, serializers
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer

class BookViewSet(ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


