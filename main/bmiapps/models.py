from django.db import models
from datetime import date


class Track(models.Model):
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    bmi = models.IntegerField(default=0)
    uploaded = models.DateField(default=date.today)
