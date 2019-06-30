from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.forms import ModelForm

class dashboard_input(models.Model):
    id = models.IntegerField(primary_key=True)
    service_service_id = models.IntegerField()
    service_service_name = models.CharField(max_length=100)
    user_user_id = models.IntegerField()
    user_caller_id = models.CharField(max_length=100)
    farmer_first_name = models.CharField(max_length=100)
    farmer_last_name = models.CharField(max_length=100)
    farmer_id = models.CharField(max_length=5)
    farmer_region = models.CharField(max_length=100)
    farmer_country = models.CharField(max_length=100)
    session_session_id = models.IntegerField()
    session_start = models.DateTimeField(max_length=100)
    category_category_id = models.IntegerField()
    category_category_name = models.CharField(max_length=100)
    input_input_value = models.IntegerField()
    farmer_city = models.CharField(max_length=100, default='null')
    farmer_longitude = models.CharField(max_length=100, default='null')
    farmer_latitude = models.CharField(max_length=100, default='null')

class Meta:
    managed = False
    db_table = 'View_dashboard_input'