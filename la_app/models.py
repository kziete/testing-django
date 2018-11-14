# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ModeloUno(models.Model):
    nombre = models.CharField(max_length=64)

    def __unicode__(self):
        return self.nombre