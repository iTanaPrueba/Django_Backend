from django.db import models


# Create your models here.
class Mobile(models.Model):
    month = models.TextField()
    network = models.CharField(max_length=2)
    plan = models.TextField()
    subscriptions = models.PositiveIntegerField()

