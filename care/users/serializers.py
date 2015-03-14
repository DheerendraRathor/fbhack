__author__ = 'dheerendra'

from rest_framework import serializers
from models import Users

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('id', 'social_id', 'first_name', 'last_name', 'email')

    def create(self, validated_data):

        try:
            user = Users.objects.get(social_id=validated_data['social_id'])
            return user
        except Users.DoesNotExist as e:
            user = Users(
                social_id = validated_data['social_id'],
                first_name = validated_data['first_name'],
                last_name = validated_data['last_name'],
                email = validated_data['email']
            )

            user.save()
            return user
