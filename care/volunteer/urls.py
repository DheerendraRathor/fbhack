__author__ = 'dheerendra'

from django.conf.urls import include, patterns, url
from rest_framework.routers import DefaultRouter
from volunteer_viewset import VolunteerViewset

router = DefaultRouter()
router.register(r'volunteer', VolunteerViewset)

urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),

    )