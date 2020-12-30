from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.
from django.http import HttpResponse
from django.shortcuts import redirect
from tensorflow import function


class mage2(models.Model):
    # title = models.CharField(max_length=200)
    images = models.ImageField(blank=True, upload_to="images", null=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.text
# class Photo(models.Model):
#     image = models.ImageField(upload_to="image")

