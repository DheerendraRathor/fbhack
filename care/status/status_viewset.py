__author__ = 'dheerendra'

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.decorators import detail_route
from django.shortcuts import get_object_or_404

from models import Status
from serializers import StatusSerializer

class StatusViewset(viewsets.ModelViewSet):

    model = Status
    serializer_class = StatusSerializer
    queryset = Status.objects.all()

    @detail_route(methods=['GET'])
    def get_nearby_status(self, request):
        latitude = request.GET['latitude']
        longitude = request.GET['longitude']
        geo = Geocoder()
        address = "%s,%s" % (str(latitude), str(longitude))
        data = geo.geocode(address=address)
        data = data[0]
        g = geocoder.google(str(data))
        g = g.json
        g = g['bbox']
        ne = g['northeast']
        sw = g['southwest']
        print(ne)
        print(sw)

        queryset = Status.objects.all().filter(latitude__gte=sw[0]).filter(latitude__lte=ne[0]).filter(longitude__gte=sw[1]).filter(longitude__lte=ne[1])
        for q in queryset:
            print(q.title)