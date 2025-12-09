from django.db import models

# Create your models here.

class users(models.Model):
    login = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    role = models.CharField(max_length=25)
    isSuperuser = models.BooleanField()
    