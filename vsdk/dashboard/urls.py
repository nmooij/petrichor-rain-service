from django.shortcuts import render
from django.urls import path

from vsdk.dashboard.fusioncharts import FusionCharts
from . import views

from django.conf.urls import url, include


urlpatterns = [
    url(r'^$', views.Chart, name = 'Chart'),
]

