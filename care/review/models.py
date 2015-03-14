from django.db import models
from users.models import Users
from status.models import Status

# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(Users)
    status = models.ForeignKey(Status)
    rate = models.IntegarField()
    comment = models.TextField(max_length=200)