from django.db import models

# Create your models here.
class Convo(models.Model):
    nombre = models.CharField(max_length=100)
    descripshort = models.CharField(max_length=300)
    descriptlong = models.CharField(max_length=50000)
    sdg = models.CharField(max_length=100)
    img_url = models.TextField()

    def __str__(self):
        return self.nombre