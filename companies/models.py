from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_lengt=255)
    nit = models.CharField(max_lengt=20)
    dian_resolution = models.CharField(max_lengt=50)
    dian_resolution_date = models.DateField()
    maximum_authorized = models.BigIntegerField()
    minimum_authorized = models.BigIntegerField()
