from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = "photo/", blank = True, null = True)

class CustomUser(AbstractUser):
    nick_name = models.CharField(max_length=200)
    university = models.CharField(max_length=100)
    location = models.CharField(max_length=300)