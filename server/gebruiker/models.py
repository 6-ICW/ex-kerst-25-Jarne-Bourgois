from django.db import models

# Create your models here.

class users(models.Model):
    login = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    # maak gebruik van een emailField
    email = models.CharField(max_length=25)
    role = models.CharField(max_length=25)
    isSuperuser = models.BooleanField()
    

# maak gebruik van default values - dat vereenvoudigd enkele zaken