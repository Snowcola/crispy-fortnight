from django.db import models
from django.utils import timezone
# Create your models here.

class Meter(models.Model):
    serial = models.IntegerField()
    badge_number = models.CharField(max_length=12)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(blank=True, null=True)
    '''
    #ert_number
    meter_type = models.CharField()
    #compliance_group = models.NumField() #should be related to the compliance_group

class MeterProof(models.Model):
    meter = models.ForeignKey('Meter_id')
    index_read = models.IntField(max_lenght=7)
    ert_read = models.IntField(max_length=7)
    open_flow_error = models.NumField()
    check_flow_error = models.NumField()
    prover_number = models.IntField()
    prover_operator = models.CharField()
    proof_date = model.DateTimeField(default=timezone.now)
'''
'''
class ComplianceGroup(models.Model):
    certified_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    c1_failures
    c2_failures
    status #active/failed/culled

class Seal
    seal_date
    extension_level
    expiry_date
''' 
