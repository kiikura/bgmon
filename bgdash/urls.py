from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from rest_framework import routers

from bgdash import views

router = routers.DefaultRouter()
router.register(r'sites', views.SiteViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns('',
  url(r'^$', TemplateView.as_view(template_name="bgdash/index.html")),
  url(r'^api/', include(router.urls)),

)


urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

from rest_framework.authtoken import views
urlpatterns += [
    url(r'^api-token-auth/', views.obtain_auth_token)
]
