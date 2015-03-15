__author__ = 'dheerendra'

from rest_framework import serializers
from models import Users

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users

    def create(self, validated_data):

        try:
            user = Users.objects.get(social_id=validated_data['social_id'])
            return user
        except Users.DoesNotExist as e:
            user = Users(**validated_data)

            user.save()
            return user
