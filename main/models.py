from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    category = models.CharField(max_length=200)
    pubisher = models.CharField(max_length=200)
    published = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title