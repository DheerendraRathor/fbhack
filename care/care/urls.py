from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'care.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('users.urls')),
    url(r'^reviews/', include('review.urls')),
    url(r'^status/', include('status.urls')),
    url(r'^volunteer/', include('volunteer.urls')),
) +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
