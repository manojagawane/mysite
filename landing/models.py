from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Distributors(models.Model):
    name = models.CharField(max_length = 256)
    address = models.CharField(max_length = 256)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("landing:detail",kwargs = {'pk':self.pk})


class Shop(models.Model):
    name = models.CharField(max_length = 256)
    address = models.CharField(max_length = 256)
    latitude = models.FloatField()
    longitude = models.FloatField()
    distributor = models.ForeignKey(Distributors,related_name='shop')

    def __str__(self):
        return self.name
