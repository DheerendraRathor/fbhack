__author__ = 'dheerendra'

from models import Status
from rest_framework import serializers
from pygeocoder import Geocoder
import geocoder
from geocoder import osm

class StatusSerializer(serializers.ModelSerializer):

    address = serializers.CharField(allow_blank=True)

    class Meta:
        model = Status
        fields = ('id', 'user', 'title', 'comment', 'rate', 'latitude', 'longitude', 'address')
        read_only_fields = ('address')

    def create(self, validated_data):
        status = Status(
            user = validated_data['user'],
            title = validated_data['title'],
            comment = validated_data['comment'],
            rate = validated_data['rate'],
            latitude = validated_data['latitude'],
            longitude = validated_data['longitude'],
            address = self.get_address(validated_data['latitude'], validated_data['longitude'])
        )
        status.save()
        return status

    def get_address(self, latitude, longitude):
        geo = Geocoder()
        address = "%s,%s" % (str(latitude), str(longitude))
        data = geo.geocode(address=address)
        data = data[0]
        return data.formatted_address


