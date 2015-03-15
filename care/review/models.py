from django.db import models
from users.models import Users
from status.models import Status

# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(Users)
    status = models.ForeignKey(Status)
    rate = models.DecimalField(max_digits=3, decimal_places=1)
    comment = models.TextField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)