# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Gift
from .forms import GiftForm, RegForm

from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login


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
            password = clean_form_data['password']
            email = clean_form_data['email']
            if password == clean_form_data['password_confirm']:
                print clean_form_data
                user = User.objects.create_user(email, email, password)
                user.save()
                new_user = authenticate(request, username=email, password=password)
                if new_user is not None:
                    login(request, new_user)
                    return HttpResponseRedirect('/track')
                else:
                    # todo - add error message
                    return HttpResponseRedirect('/track/register')
            else:
                # todo - add error message
                return HttpResponseRedirect('/track/register')
    else:
        form = RegForm()
    return render(request, 'gifttrack/register.html', {'form': form})
