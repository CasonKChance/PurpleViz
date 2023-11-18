from django.db import models

# Create your models here.
class Mat(models.Model):
    matWidth = models.FloatField()
    matLength = models.FloatField()

    @property
    def matSize(self):
        return self.matWidth * self.matLength