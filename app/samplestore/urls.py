from django.conf.urls import url, include
from django.views.defaults import page_not_found
from django.contrib import admin

from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'subjects', views.SubjectViewSet)
router.register(r'sampletypes', views.SampleTypeViewSet)
router.register(r'samples', views.SampleViewSet)
router.register(r'aliquottypes', views.AliquotTypeViewSet)
router.register(r'aliquotqualities', views.AliquotQualityViewSet)
router.register(r'aliquots', views.AliquotViewSet)
router.register(r'assaytypes', views.AssayTypeViewSet)
router.register(r'assaystatuses', views.AssayStatusViewSet)
router.register(r'assays', views.AssayViewSet)
router.register(r'sequencingfiles', views.SequencingFileViewSet)
router.register(r'attachments', views.AttachmentViewSet)
router.register(r'intrepretations', views.InterpretationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/login/', page_not_found, {'exception': Exception('Admin form login disabled.')}),
    url(r'^admin/', admin.site.urls)
]