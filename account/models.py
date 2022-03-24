from django.db import models
from django.contrib.auth.models import User


class UserModel(models.Model):
    GENDER_ID = [
        ('M', 'male'),
        ('F', 'female'),
    ]
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_ID, null=True)
    image = models.ImageField()
    email = models.EmailField()
