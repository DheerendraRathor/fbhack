from django.db import models
from users.models import Users
from status.models import Status


class Volunteer(models.Model):
    user = models.ForeignKey(Users)
    status = models.ForeignKey(Status)

    class Meta:
    	unique_together = (("user", "status"),)

# Create your models here.
