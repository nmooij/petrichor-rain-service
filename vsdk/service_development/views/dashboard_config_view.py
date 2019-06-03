from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.http.response import HttpResponseRedirect
from django.views.generic.edit import CreateView

from ..models import dashboard_input, DashboardConfig, DashboardConfigForm

class CreateDashboardInputModelView (CreateView):
    model = DashboardConfig
    form_class = DashboardConfigForm
    template_name = 'service_development/templates/"dashboard_config_template.html'