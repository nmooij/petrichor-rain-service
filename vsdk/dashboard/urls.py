from django.shortcuts import render
from django.urls import path

from vsdk.dashboard.fusioncharts import FusionCharts
from . import views

from django.conf.urls import url, include

# urlpatterns = [
    # path('', views.index, name='index'),
# ]

urlpatterns = [
    url(r'^$', views.myFirstChart, name = 'demo'),
]
