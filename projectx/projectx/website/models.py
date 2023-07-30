from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils import timezone

from django.contrib.auth import get_user_model

User = get_user_model

# Create your models here.

#class Poem(models.Model):
#    title = models.CharField(max_length=100)
#    content = models.TextField()

#    def __str__(self):
#        return self.title
    

class CustomUser(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default=None)
    GENDER_CHOICES = [
        ("Мужской", "Мужской"),
        ("Женский", "Женский"),
        ("Кот", "Кот")
    ]
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    birthday = models.DateField()

class CommentSection(models.Model):
    comment = models.CharField(max_length=5000)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    verse_title = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.comment

