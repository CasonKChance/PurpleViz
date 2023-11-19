from django.db import models

# Create your models here.
class Test(models.Model):
    toleranceLevel = models.IntegerField()
    matWidth = models.FloatField(default=0.0)
    matLength = models.FloatField(default=0.0)