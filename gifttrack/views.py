# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Gift, GiftList, GiftListFields
from .forms import GiftForm, RegForm, LoginForm, GiftListForm

from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'gifttrack/index.html')


@login_required
def user_page(request):
    if request.method == 'POST':
        form = GiftListForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['description'] == "":
                description = "No Description"
            else:
                description = form.cleaned_data['description']
            gift_list = GiftList(
                name=form.cleaned_data['name'],
                description=description,
                user=request.user
            )
            gift_list.save()
            return HttpResponseRedirect('/user')
    else:
        form = GiftListForm()
        user_gift_lists = GiftList.objects.filter(user=request.user)
        context = {'user_gift_lists': user_gift_lists, 'form': form}
        return render(request, 'gifttrack/user_page.html', context)


# todo - ensure ownership of list
@login_required
def gift_listing(request, list_id):
    if request.method == 'POST':
        form = GiftForm(request.POST)
        if form.is_valid():
            gift_list = GiftList.objects.get(id=int(list_id))
            gift = Gift(
                gift_desc=form.cleaned_data['gift_desc'],
                gift_from=form.cleaned_data['gift_from'],
                gift_notes=form.cleaned_data['gift_notes'],
                gift_list=gift_list
            )
            gift.save()
            return HttpResponseRedirect('/list/{}'.format(list_id))
    else:
        form = GiftForm()
        gifts = Gift.objects.filter(
            gift_list__user=request.user,
            gift_list__id=int(list_id)
        )
        context = {'gifts': gifts, 'form': form, 'list_id': list_id}
        return render(request, 'gifttrack/gift_page.html', context)


def login_user(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/user')
            else:
                messages.error(request, 'Invalid username/password')
                return HttpResponseRedirect('/login')
    else:
        form = LoginForm()
        return render(request, 'gifttrack/login.html', {'form': form})


def logout_user(request):
    if request.user.is_authenticated():
        logout(request)
        messages.info(request, 'Logged out')
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')


def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
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
                        return HttpResponseRedirect('/')
                    else:
                        messages.error(
                            request,
                            'An error occurred in registration'
                        )
                        return HttpResponseRedirect('/register')
                else:
                    messages.error(request, 'Username already exists')
                    return HttpResponseRedirect('/register')
            else:
                messages.error(request, 'Please enter matching passwords')
                return HttpResponseRedirect('/register')
    else:
        form = RegForm()
    return render(request, 'gifttrack/register.html', {'form': form})
