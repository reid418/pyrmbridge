from django.conf.urls import url, include
from rest_framework import routers
from pyrmbridge import views
from pyrmbridge import models

router = routers.DefaultRouter()
router.register(r'broadlinkdevices', views.BroadlinkDeviceViewSet)
router.register(r'broadlinkcommands', views.BroadlinkCommandViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^test/$', views.view),
]
