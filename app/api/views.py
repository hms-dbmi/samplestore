from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework import viewsets

from api.permissions import IsAssociatedUser

from api.serializers import SubjectSerializer
from api.serializers import SampleTypeSerializer
from api.serializers import SampleSerializer
from api.serializers import AliquotTypeSerializer
from api.serializers import AliquotQualitySerializer
from api.serializers import AliquotSerializer
from api.serializers import AssayTypeSerializer
from api.serializers import AssayStatusSerializer
from api.serializers import AssaySerializer
from api.serializers import SequencingFileSerializer
from api.serializers import AttachmentSerializer
from api.serializers import InterpretationSerializer

from api.models import Subject
from api.models import SampleType
from api.models import Sample
from api.models import AliquotType
from api.models import AliquotQuality
from api.models import Aliquot
from api.models import AssayType
from api.models import AssayStatus
from api.models import Assay
from api.models import SequencingFile
from api.models import Attachment
from api.models import Interpretation

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (permissions.IsAuthenticated, IsAssociatedUser,)
    filter_fields = ('external_id',)

class SampleTypeViewSet(viewsets.ModelViewSet):
    queryset = SampleType.objects.all()
    serializer_class = SampleTypeSerializer
    permission_classes = (permissions.IsAuthenticated, IsAssociatedUser,)

class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    permission_classes = (permissions.IsAuthenticated, IsAssociatedUser,)
    filter_fields = ('subject__external_id',)

class AliquotTypeViewSet(viewsets.ModelViewSet):
    queryset = AliquotType.objects.all()
    serializer_class = AliquotTypeSerializer
    permission_classes = (permissions.IsAuthenticated, IsAssociatedUser,)

class AliquotQualityViewSet(viewsets.ModelViewSet):
    queryset = AliquotQuality.objects.all()
    serializer_class = AliquotQualitySerializer
    permission_classes = (permissions.IsAuthenticated, IsAssociatedUser,)

class AliquotViewSet(viewsets.ModelViewSet):
    queryset = Aliquot.objects.all()
    serializer_class = AliquotSerializer
    permission_classes = (permissions.IsAuthenticated, IsAssociatedUser,)

class AssayTypeViewSet(viewsets.ModelViewSet):
    queryset = AssayType.objects.all()
    serializer_class = AssayTypeSerializer
    permission_classes = (permissions.IsAuthenticated, IsAssociatedUser,)

class AssayStatusViewSet(viewsets.ModelViewSet):
    queryset = AssayStatus.objects.all()
    serializer_class = AssayStatusSerializer
    permission_classes = (permissions.IsAuthenticated, IsAssociatedUser,)

class AssayViewSet(viewsets.ModelViewSet):
    queryset = Assay.objects.all()
    serializer_class = AssaySerializer
    permission_classes = (permissions.IsAuthenticated, IsAssociatedUser,)
    filter_fields = ('sample__subject__external_id',)

class SequencingFileViewSet(viewsets.ModelViewSet):
    queryset = SequencingFile.objects.all()
    serializer_class = SequencingFileSerializer
    permission_classes = (permissions.IsAuthenticated, IsAssociatedUser,)

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = (permissions.IsAuthenticated, IsAssociatedUser,)

class InterpretationViewSet(viewsets.ModelViewSet):
    queryset = Interpretation.objects.all()
    serializer_class = InterpretationSerializer
    permission_classes = (permissions.IsAuthenticated, IsAssociatedUser,)
