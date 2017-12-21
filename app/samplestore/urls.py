from django.conf.urls import url, include
from django.views.defaults import page_not_found
from django.contrib import admin

from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/login/', page_not_found, {'exception': Exception('Admin form login disabled.')}),
    url(r'^admin/', admin.site.urls)
]