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


class AvgRainPerCountry(models.Model):
   id = models.IntegerField(primary_key=True)
   Rainfall = models.IntegerField()
   Country = models.CharField(max_length=100)
   Month = models.CharField(max_length=100)
   
