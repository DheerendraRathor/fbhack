__author__ = 'dheerendra'

from django.conf.urls import include, patterns, url
from rest_framework.routers import DefaultRouter
from review_viewset import ReviewViewset

router = DefaultRouter()
router.register(r'review', ReviewViewset)

urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),

    )