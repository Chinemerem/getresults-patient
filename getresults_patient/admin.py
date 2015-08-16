from django.contrib import admin

from getresults.admin import admin_site

from .models import Patient


class PatientAdmin(admin.ModelAdmin):

    date_hierarchy = 'registration_datetime'

    list_display = ('patient_identifier', 'registration_datetime')
    list_filter = ('registration_datetime', )
    search_fields = ('patient_identifier', )
admin_site.register(Patient, PatientAdmin)
