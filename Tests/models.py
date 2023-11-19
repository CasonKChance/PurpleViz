from django.db import models

# Create your models here.

class Tests(models.Model):
    testTotal = models.IntegerField()
    testCount = models.IntegerField()