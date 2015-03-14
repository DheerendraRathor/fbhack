__author__ = 'dheerendra'

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.decorators import detail_route
from django.shortcuts import get_object_or_404

from models import Users
from serializers import UsersSerializer

class UserViewset(viewsets.ModelViewSet):

    model = Users
    serializer_class = UsersSerializer
    queryset = Users.objects.all()
