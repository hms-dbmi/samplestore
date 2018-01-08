import uuid
from django.db import models

class Subject(models.Model):
    """
    This represents a person.
    """
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    external_id = models.CharField(max_length=255)

    def __str__(self):
        return "%s %s" % (self.uuid, self.external_id)

class SampleType(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2048, blank=True, null=True)
    location = models.CharField(max_length=255)

    def __str__(self):
        return "%s %s %s" % (self.code, self.name, self.location)

class Sample(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    obtained = models.DateTimeField()
    description = models.CharField(max_length=2048, blank=True, null=True)
    sample_type = models.ForeignKey(SampleType, on_delete=models.PROTECT, related_name="sample_sample_type")
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name="sample_subject")

    def __str__(self):
        return "%s %s %s" % (self.name, self.sample_type.name, self.uuid)

class AliquotType(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2048, blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.code, self.name)

class AliquotQuality(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2048, blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.code, self.name)

class Aliquot(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    prepared = models.DateTimeField()
    description = models.CharField(max_length=2048, blank=True, null=True)
    lab_name = models.CharField(max_length=255, blank=True, null=True)
    prepared_by = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.CharField(max_length=255, blank=True, null=True)
    sample = models.ForeignKey(Sample, on_delete=models.PROTECT, related_name="aliquot_sample")
    aliquot_type = models.ForeignKey(AliquotType, on_delete=models.PROTECT, related_name="aliquot_aliquot_type")
    aliquot_quality = models.ForeignKey(AliquotQuality, on_delete=models.PROTECT, related_name="aliquot_aliquot_quality")

    def __str__(self):
        return "%s %s" % (self.name, self.uuid)

class AssayType(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2048, blank=True, null=True)

    def __str__(self):
        return "%s" % self.name

class AssayStatus(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2048, blank=True, null=True)

    def __str__(self):
        return "%s" % self.name

class Assay(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    datetime = models.DateTimeField()
    lab_name = models.CharField(max_length=255, blank=True, null=True)
    rationale = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=2048, blank=True, null=True)
    technician_id = models.CharField(max_length=255, blank=True, null=True)
    completed = models.DateTimeField() # is this correction?
    equipment_id = models.CharField(max_length=255, blank=True, null=True)
    coverage = models.CharField(max_length=255, blank=True, null=True)
    reanalysis_id = models.ForeignKey("self", on_delete=models.PROTECT, blank=True, null=True, related_name="assay_reanalysis_id")
    assay_type = models.ForeignKey(AssayType, on_delete=models.PROTECT, related_name="assay_assay_type")
    assay_status = models.ForeignKey(AssayStatus, on_delete=models.PROTECT, related_name="assay_assay_status")
    aliquot = models.ForeignKey(Aliquot, on_delete=models.PROTECT, related_name="assay_aliquot")
    sample = models.ForeignKey(Sample, on_delete=models.PROTECT, related_name="assay_sample")

    def __str__(self):
        return "%s" % self.uuid

class SequencingFile(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=255)
    fileservice_uuid = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField()
    md5 = models.CharField(max_length=1000, blank=True, null=True, default=" ")
    assay = models.ForeignKey(Assay, on_delete=models.PROTECT, related_name="sequencingfile_assay")

    def __str__(self):
        return "%s %s" % (self.uuid, self.file_name)

class Attachment(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=255)
    description = models.CharField(max_length=2048, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField()
    assay = models.ForeignKey(Assay, on_delete=models.PROTECT, related_name="attachment_assay")

    def __str__(self):
        return "%s %s" % (self.uuid, self.file_name)

class Interpretation(models.Model):
    file_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField()
    assay = models.ForeignKey(Assay, on_delete=models.PROTECT, related_name="interpretation_assay")

    def __str__(self):
        return "%s %s" % (self.file_name, self.file_uuid)
