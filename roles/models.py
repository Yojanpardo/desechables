from django.db import models

# Create your models here.

class Rol(models.Model):
    name = models.CharField(max_lengt=96)
    description = models.TextField(max_lengt=255)
