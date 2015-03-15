__author__ = 'dheerendra'

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.decorators import detail_route
from django.shortcuts import get_object_or_404
from review.models import Review

from models import Status
from serializers import StatusSerializer
from django.db.models import Avg, Count, Sum

class StatusViewset(viewsets.ModelViewSet):

    model = Status
    serializer_class = StatusSerializer
    queryset = Status.objects.all()

    @detail_route(methods=['GET'])
    def get_status(self, request,pk):
        latitude = float(request.GET['latitude'])
        longitude = float(request.GET['longitude'])
        #address = "%s,%s" % (str(latitude), str(longitude))
        ne = (latitude + (0.008983) * 1, longitude + (0.015060) * 1)
        sw = (latitude - (0.008983) * 1, longitude - (0.015060) * 1)

        queryset = Status.objects.all().filter(latitude__gte=sw[0]).filter(latitude__lte=ne[0]).filter(longitude__gte=sw[1]).filter(longitude__lte=ne[1])
        serializer = StatusSerializer(queryset, many=True)
        return Response(serializer.data)

    @detail_route(methods=['POST'])
    def upload_image(self, request, pk):
        status = get_object_or_404(Status, pk=pk)
        status.image = request.FILES.get('image')
        status.save()
        serializer = StatusSerializer(status)
        return Response(serializer.data)

    @detail_route(methods=['GET'])
    def average(self, request, pk):
        avg = Review.objects.all().filter(status__id=pk).aggregate(average=Avg('rate'))
        return Response(avg)

    @detail_route(methods=['GET'])
    def graph(self, request, pk):
        latitude = float(request.GET['latitude'])
        longitude = float(request.GET['longitude'])
        #address = "%s,%s" % (str(latitude), str(longitude))
        ne = (latitude + (0.008983) * 1, longitude + (0.015060) * 1)
        sw = (latitude - (0.008983) * 1, longitude - (0.015060) * 1)

        queryset = Status.objects.all()\
            .filter(latitude__gte=sw[0]).filter(latitude__lte=ne[0]).filter(longitude__gte=sw[1]).filter(longitude__lte=ne[1])\
            .extra({'date_created' : "date(status_status.created_on)"})\
            .values('date_created')\
            .annotate(avg_rate=Avg('rate')).annotate(count=Count('id')).annotate(weight=Avg('review__rate'))
        total = 0
        cumulative = 0.0

        for item in queryset:
            if item['weight'] is None:
                item['weight'] = 0.75
            item['cumulative'] = (total*cumulative + item['count']*item['avg_rate']*item['weight'])/(total + item['count'])
            total = total + item['count']
            cumulative = item['cumulative']

        #serializers = StatusSerializer(queryset, many=True)
        return Response(queryset)