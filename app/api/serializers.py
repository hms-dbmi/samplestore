from rest_framework import serializers

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

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('uuid', 'external_id')

class SampleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleType
        fields = ('code', 'name', 'description', 'location')

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ('uuid', 'name', 'obtained', 'description', 'sample_type', 'subject')

class AliquotTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AliquotType
        fields = ('code', 'name', 'description')

class AliquotQualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AliquotQuality
        fields = ('code', 'name', 'description')

class AliquotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aliquot
        fields = ('uuid', 'name', 'prepared', 'description', 'lab_name', 'prepared_by', 'quantity', 'sample', 'aliquot_type', 'aliquot_quality')

class AssayTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssayType
        fields = ('name', 'description')

class AssayStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssayStatus
        fields = ('name', 'description')

class AssaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Assay
        fields = ('uuid', 'datetime', 'lab_name', 'rationale', 'notes', 'technician_id', 'completed', 'equipment_id', 'coverage', 'reanalysis_id', 'assay_type', 'assay_status', 'aliquot', 'sample')

class SequencingFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SequencingFile
        fields = ('uuid', 'file_name', 'file_type', 'fileservice_uuid', 'location', 'created', 'md5', 'assay')

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ('uuid', 'file_name', 'file_type', 'description', 'location', 'created', 'assay')

class InterpretationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interpretation
        fields = ('file_uuid', 'file_name', 'file_type', 'location', 'created', 'assay')