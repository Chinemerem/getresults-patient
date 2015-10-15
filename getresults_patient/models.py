from django.db import models
from django_crypto_fields.fields import FirstnameField, LastnameField

from edc_base.model.models import BaseUuidModel
from edc_base.audit_trail import AuditTrail
from edc_constants.choices import GENDER

from .identifiers import PatientIdentifier
from django.utils import timezone


class Patient(BaseUuidModel):

    patient_identifier = models.CharField(
        max_length=25)

    first_name = FirstnameField(
        null=True,
        blank=True,
        verbose_name="First Name")

    last_name = LastnameField(
        null=True,
        blank=True,
        verbose_name="Last Name")

    protocol = models.CharField(
        max_length=25,
        null=True)

    account = models.CharField(
        max_length=25,
        null=True)

    registration_datetime = models.DateTimeField(
        default=timezone.now)

    gender = models.CharField(
        max_length=10,
        choices=GENDER,
        null=True)

    dob = models.DateField(
        null=True)

    identity = models.CharField(
        max_length=25,
        null=True)

    history = AuditTrail()

    def save(self, *args, **kwargs):
        if not self.id and not self.patient_identifier:
            self.patient_identifier = PatientIdentifier().identifier
        super(Patient, self).save(*args, **kwargs)

    def __str__(self):
        return self.patient_identifier

    class Meta:
        app_label = 'getresults_patient'
        db_table = 'getresults_patient'
