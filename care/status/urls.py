__author__ = 'dheerendra'

from django.conf.urls import include, patterns, url
from rest_framework.routers import DefaultRouter
from status_viewset import StatusViewset

router = DefaultRouter()
router.register(r'status', StatusViewset)

urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),

    )