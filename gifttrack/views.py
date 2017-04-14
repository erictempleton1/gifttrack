# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Gift
from django.shortcuts import render


def index(request):
    all_gifts = Gift.objects.all()
    context = {'all_gifts': all_gifts}
    return render(request, 'gifttrack/index.html', context)
