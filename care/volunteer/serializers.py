__author__ = 'dheerendra'

from rest_framework import serializers
from models import Volunteer

class VolunteerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Volunteer