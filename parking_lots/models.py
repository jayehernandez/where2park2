# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Lots(models.Model):
    auto_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
