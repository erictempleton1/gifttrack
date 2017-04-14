# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Gift
from .forms import GiftForm, RegForm
from django.contrib.auth.models import User

from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    all_gifts = Gift.objects.all()
    context = {'all_gifts': all_gifts}
    return render(request, 'gifttrack/index.html', context)


def create(request):
    if request.method == 'POST':
        form = GiftForm(request.POST)
        if form.is_valid():
            clean_form_data = form.cleaned_data
            gift_obj = Gift(
                gift_desc=clean_form_data['gift_desc'],
                gift_from=clean_form_data['gift_from'],
                gift_notes=clean_form_data['gift_notes'],
            )
            gift_obj.save()
            return HttpResponseRedirect('/track')
    else:
        form = GiftForm()
    return render(request, 'gifttrack/create.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        print form
        if form.is_valid():
            clean_form_data = form.cleaned_data
            print clean_form_data
            return HttpResponseRedirect('/track')
    else:
        form = RegForm()
    return render(request, 'gifttrack/register.html', {'form': form})
