__author__ = 'dheerendra'

from models import Status
from rest_framework import serializers
from pygeocoder import Geocoder
from users.serializers import UsersSerializer

class StatusSerializer(serializers.ModelSerializer):

    address = serializers.CharField(allow_blank=True)
    user = UsersSerializer()
    class Meta:
        model = Status
        read_only_fields = ('address')

    def create(self, validated_data):
        status = Status(**validated_data)
        status.address = self.get_address(validated_data['latitude'], validated_data['longitude'])
        status.save()
        return status

    def get_address(self, latitude, longitude):
        geo = Geocoder()
        address = "%s,%s" % (str(latitude), str(longitude))
        data = geo.geocode(address=address)
        data = data[0]
        return data.formatted_address


