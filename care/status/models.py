from django.db import models
from users.models import Users
import uuid
# Create your models here.

def get_filename(instance, filename):
    print "HERE"
    unique_id = uuid.uuid1()
    unique_id = unique_id.hex
    return  str(unique_id) + ".png"


class Status(models.Model):
    user = models.ForeignKey(Users)
    title = models.TextField()
    comment = models.TextField()
    rate = models.DecimalField(max_digits=3, decimal_places=1)
    latitude = models.DecimalField(max_digits=20, decimal_places=15)
    longitude = models.DecimalField(max_digits=20, decimal_places=15)
    address = models.TextField()
    image = models.ImageField(upload_to=get_filename, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)