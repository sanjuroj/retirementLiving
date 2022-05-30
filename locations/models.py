from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db.models import PointField
from address.models import AddressField

OWNERSHIP_TYPES = {
    0: 'Private Equity',
    1: 'Direct'
}


class ParentCompany(models.Model):
    name = models.TextField('Parent Company', max_length=500)
    owner_type = models.IntegerField('Owner Type')


class Facility(models.Model):

    name = models.TextField('Facility Name', max_length=500)
    address = AddressField('Address')
    geo_point = PointField()
    parent_company = models.ForeignKey(ParentCompany, null=True, on_delete=models.SET_NULL)
    ownership_type = models.IntegerField('Ownership Type', null=True)


class CareLevel(models.Model):
    CARE_LEVEL_TYPES = {
        0: 'Independent Living',
        1: 'Assisted Living',
        2: 'Memory Care'
    }

    name = models.TextField(max_length=500)
    type = models.IntegerField()
    facility = models.ForeignKey(Facility, on_delete=models.SET_NULL, related_name='care_levels')


class CareLevelData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    staff_ratio = models.DecimalField()

