from django.db import models

# Create your models here.
class Test(models.Model):
    testID = models.IntegerField()
    toleranceLevel = models.IntegerField()