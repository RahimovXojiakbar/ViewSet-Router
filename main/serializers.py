from django.contrib.auth import get_user_model
from . import models
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

class BookSerializer(ModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'
