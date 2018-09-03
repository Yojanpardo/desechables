from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_lengt=20)
    description = models.TextField(max_lengt=255)
    roles = models.ManyToManyField('roles.Rol')
    company = models.ForeignKey('companies.Company')
