from django.db import models

# Create your models here.
class Attribute(models.Model):
    name = models.CharField(max_length=200)
    score = models.DecimalField(max_digits=2, decimal_places=1)

class RatedObject(models.Model):
    name = models.CharField(max_length=200)
    publish_date = models.DateField(max_length=200)

class RatedModel(models.Model):
    name = models.CharField(max_length=200)
    publish_date = models.DateField(max_length=200)
    attributes = models.ForeignKey(Attribute, blank=True, null=True)
    rated_objects = models.ForeignKey(RatedObject, blank=True, null=True)