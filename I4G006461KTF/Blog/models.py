from typing import Text
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(User)
    Created_date = models.DateTimeFIeld()
    Published_date = models.DateTimeField()
