from django.db import models

# Create your models here.

class Users(models.Model):
    social_id = models.CharField(max_length=128, unique=True)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
