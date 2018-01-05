from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=300, help_text="Enter your Statement")
    #text = models.TextField(help_text="Enter your Statement")
    author = models.ForeignKey('auth.User')


    def __str__(self):
        return self.text
