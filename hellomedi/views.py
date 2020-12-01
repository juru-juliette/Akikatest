# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import *
from .forms import NewsLetterForm 
from .email import send_welcome_email
from django.core.mail import send_mail

# Create your views here.

# def welcome(request):
#     # return HttpResponse('Welcome to Hello medical')
#     return render(request, 'index.html')

def news_update(request):
   
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('news_update')
    else:
        form = NewsLetterForm()
    return render(request, 'index.html', {"letterForm":form})
