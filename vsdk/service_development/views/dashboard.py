from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse
from django.views.generic import View
from django.http.response import HttpResponseRedirect

from ..models import *

from . import base


class DashboardView(View):

    def index(request):
     return HttpResponse('This is the VoiceXML generator')