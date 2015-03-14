__author__ = 'dheerendra'

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.decorators import detail_route
from django.shortcuts import get_object_or_404

from models import Volunteer
from serializers import Volunteererializer

class ReviewViewset(viewsets.ModelViewSet):

    model = Volunteer
    serializer_class = VolunteerSerializer
    queryset = Volunteer.objects.all()