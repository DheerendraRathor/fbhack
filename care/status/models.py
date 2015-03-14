from django.db import models
from users.models import Users

# Create your models here.

class Status(models.Model):
    user = models.ForeignKey(Users)
    title = models.TextField()
    comment = models.TextField()
    rate = models.DecimalField(max_digits=3, decimal_places=1)
    latitude = models.DecimalField(max_digits=12, decimal_places=8)
    longitude = models.DecimalField(max_digits=12, decimal_places=8)
    address = models.TextField()
