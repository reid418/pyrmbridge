from __future__ import unicode_literals
from django.db import models


class BroadlinkCommand(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    command = models.TextField()


class BroadlinkDevice(models.Model):
    ip = models.CharField(max_length=30)
    port = models.IntegerField()
    name = models.CharField(max_length=30)
    description = models.TextField()
    model = models.CharField(max_length=30)
    mac = models.CharField(max_length=30)
