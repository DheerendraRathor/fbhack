from django.db import models
from users.models import Users

# Create your models here.

class Status(models.Model):
    user = models.ForeignKey(Users)
    title = models.TextField()
