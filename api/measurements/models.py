from django.db import models

# Create your models here.
class Temperature (models.Model):
    value = models.FloatField()
    date = models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length = 64)

class Config (models.Model):
    name = models.CharField(max_length = 64)
    mac = models.CharField(max_length = 32)
    enabled = models.BooleanField(default = True)
