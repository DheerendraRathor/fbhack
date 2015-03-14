__author__ = 'dheerendra'

from models import Status
from rest_framework import serializers

class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ('id', 'user', 'title', 'comment', 'rate', 'latitude', 'longitude', 'address')