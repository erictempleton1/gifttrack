# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

from datetime import datetime


@python_2_unicode_compatible
class Gift(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gift_desc = models.CharField(max_length=500)
    gift_from = models.CharField(max_length=200)
    gift_notes = models.CharField(max_length=500)
    save_date = models.DateTimeField(default=datetime.now)
    edit_date = models.DateTimeField()

    def __str__(self):
        return self.gift_desc
