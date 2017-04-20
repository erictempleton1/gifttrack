# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Gift
from .forms import GiftForm, RegForm

from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login


def index(request):
    all_gifts = Gift.objects.all()
    all_users = User.objects.all()
    context = {'all_gifts': all_gifts, 'all_users': all_users}
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
            messages.success(request, 'Gift added!')
            return HttpResponseRedirect('/track')
    else:
        form = GiftForm()
    return render(request, 'gifttrack/create.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            clean_form_data = form.cleaned_data
            password = clean_form_data['password']
            email = clean_form_data['email']
            if password == clean_form_data['password_confirm']:
                user_exists = User.objects.filter(username=email).exists()
                if not user_exists:
                    user = User.objects.create_user(email, email, password)
                    user.save()
                    # todo - maybe remove auth check here and go straight to login?
                    new_user = authenticate(
                        request, 
                        username=email, 
                        password=password
                    )
                    if new_user is not None:
                        login(request, new_user)
                        return HttpResponseRedirect('/track')
                    else:
                        messages.error(
                            request,
                            'An error occurred in registration'
                        )
                        return HttpResponseRedirect('/track/register')
                else:
                    messages.error(request, 'Username already exists')
                    return HttpResponseRedirect('/track/register')
            else:
                messages.error(request, 'Please enter matching passwords')
                return HttpResponseRedirect('/track/register')
    else:
        form = RegForm()
    return render(request, 'gifttrack/register.html', {'form': form})
