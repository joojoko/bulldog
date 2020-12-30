from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.
from django.http import HttpResponse
from django.shortcuts import redirect
from tensorflow import function


class mage(models.Model):
    # title = models.CharField(max_length=200)
    images = models.ImageField(blank=True, upload_to="images", null=True)

    # def __str__(self):
    #     return self.title
# class Photo(models.Model):
#     image = models.ImageField(upload_to="image")

