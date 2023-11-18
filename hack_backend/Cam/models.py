from django.db import models

# Create your models here.
class Cam(models.Model):
    pixelWidth = models.FloatField()
    pixelLength = models.FloatField()

    @property
    def pixelSize(self):
        return self.pixelWidth * self.pixelLength