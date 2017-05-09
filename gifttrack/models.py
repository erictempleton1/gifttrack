# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

from datetime import datetime


@python_2_unicode_compatible
class GiftList(models.Model):
    name = models.CharField(max_length=500)
    save_date = models.DateTimeField(default=timezone.now)
    edit_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class GiftListFields(models.Model):
    name = models.CharField(max_length=150)
    save_date = models.DateTimeField(default=datetime.now)
    edit_date = models.DateTimeField(default=datetime.now)
    gift_list = models.ForeignKey(GiftList, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Gift(models.Model):
    gift_desc = models.CharField(max_length=500)
    gift_from = models.CharField(max_length=200)
    gift_notes = models.CharField(max_length=500)
    save_date = models.DateTimeField(default=datetime.now)
    edit_date = models.DateTimeField(default=datetime.now)
    gift_list = models.ForeignKey(GiftList, on_delete=models.CASCADE)

    def __str__(self):
        return self.gift_desc
