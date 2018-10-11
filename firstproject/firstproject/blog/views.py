# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .form import ContactForm,SignUpForm

from django.conf import settings

from django.core.mail import send_mail

# Create your views here.


def home(request):
    title = 'welcome'
    #if request.user.is_authenticated():
      #title = "shaymaa %s" %(request.user)
    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }
    if form.is_valid():
        #form.save()
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")
        if not instance.full_name:
             full_name = "Erbil"
        instance.save()
        context = {
             "title": "Thanks for registration"

            }
    return render(request, "home.html", context)
def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
      #email = form.cleaned_data.get("email")
      # message = form.cleaned_data.get("message")
      # full_name = form.cleaned_data.get("full_name")
       #print email , message , full_name
        #for key,value in form.cleaned_data.iteritems():
            #print key, value
      form_email = form.cleaned_data.get("email")
      form_message = form.cleaned_data.get("message")
      form_full_name = form.cleaned_data.get("full_name")
      Subject = 'mail from django'
      from_email = settings.EMAIL_HOST_USER
      to_email = [from_email,'shaymaaragab1234@gmail.com']
      contact_message = "%s: %s via %s"%(
          form_full_name,
          form_message,
          form_email)
      send_mail(
          Subject,
          contact_message,
          form_email,
          to_email,
          fail_silently=True)

    context = {
        "form": form
    }
    return render(request, 'forms.html', context)
