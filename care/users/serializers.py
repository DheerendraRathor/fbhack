__author__ = 'dheerendra'

from rest_framework import serializers
from models import Users

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('id', 'social_id', 'first_name', 'last_name', 'email')