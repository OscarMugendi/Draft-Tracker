import os
import json
from decouple import config, Csv
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.templatetags.static import static
from django.http  import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.http  import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.defaulttags import register

from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from .models import *

import datetime as dt

# Create your views here.

def home(request):
    current_user = request.user

    return render(request, 'home.html')


@login_required(login_url='/accounts/login/')
def profile(request, username):
    
    return render(request, 'profile.html')


@login_required(login_url='/accounts/login/')
def update_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()

            return redirect('profile', user.username)
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'update_profile.html', {'form': form})
