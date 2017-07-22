# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.timezone import localtime
from django.utils import timezone

# Create your views here.

from .models import Lots

def Home(request):
    variables['lol'] = 'lol';
    return render(request, 'home.html', variables);
