from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.utils.safestring import mark_safe






class Dashboard(models.Model):
    dashboard_name = models.CharField(_('DashboardName'),max_length=100, unique = True)
    dashboard_code = models.CharField(_('DashboardCode'),max_length=10, unique = True)
    

    class Meta:
        verbose_name = _('Dashboard')

    