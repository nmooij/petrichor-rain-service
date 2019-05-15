from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DashboardConfig(AppConfig):
    name = 'vsdk.dashboard'
    verbose_name = _("Dashboards")
