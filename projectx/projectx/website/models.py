from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#class Poem(models.Model):
#    title = models.CharField(max_length=100)
#    content = models.TextField()

#    def __str__(self):
#        return self.title
    

class CustomUser(AbstractUser):
    pass

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ("male", "Мужской"),
        ("female", "Женский")
    ]
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    birthday = models.DateField()

