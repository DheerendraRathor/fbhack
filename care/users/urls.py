__author__ = 'dheerendra'

from django.conf.urls import include, patterns, url
from rest_framework.routers import DefaultRouter
from user_viewset import UserViewset

router = DefaultRouter()
router.register(r'user', UserViewset)

urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),

    )