from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from django.core.mail import send_mail

from datetime import datetime
import datetime as dt
import requests


from django.views.decorators.csrf import csrf_exempt
import time

#from main.ray_bns import GetAddress, GetPrice



#from .forms import UserForm


def IndexView(request):

    if request.method == "POST":
        pass

    else:
            
        context = {}
        return render(request, "main/index.html", context )


def ResultView(request, domain_name):

    if request.method == "POST":
        pass

    else:
        context = {}

        return render(request, "main/result.html", context )


def BuyView(request, domain_name):

    if request.method == "POST":
        pass

    else:
        context = {}

        return render(request, "main/buy.html", context )


def RegisteredView(request):
    if request.method == "POST":
        pass
    else:
        context = {}
        return render(request, "main/registered.html", context )


def ManageView(request, domain_name):
    if request.method == "POST":
        pass

    else:           
        context = {}
        return render(request, "main/manage.html", context )


def Transfer2View(request, domain_name, domain_namek):
    if request.method == "POST":
        pass

    else:

        context = {}
        return render(request, "main/transfer2.html", context )
