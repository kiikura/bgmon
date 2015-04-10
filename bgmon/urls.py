from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'bgmon.views.home', name='home'),
    url(r'^bgdash/', include('bgdash.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
