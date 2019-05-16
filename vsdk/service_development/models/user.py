from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

#from phonenumber_field.modelfields import PhoneNumberField

from . import Language
from . import VoiceService


class KasaDakaUser(models.Model):
    """
    User that belongs to a Voice Service on this system
    """
    caller_id = models.CharField(_('Phone number'),max_length=100, unique = True)
    farmer_id = models.CharField(_('FarmerID'),max_length=5, unique = True)
    first_name = models.CharField(_('First name'), max_length = 100, blank = True)
    last_name = models.CharField(_('Last name'), max_length=100, blank = True)
    creation_date = models.DateTimeField(_('Date created'),auto_now_add = True)
    modification_date = models.DateTimeField(_('Date last modified'),auto_now = True)
    region = models.CharField(_('Region'), max_length=100, blank = True)
    country = models.CharField(_('Country'), max_length=100, blank = True)
    longitude = models.CharField(_('Longitude'), max_length=100, blank = True)
    latitude = models.CharField(_('Latitude'), max_length=100, blank = True)
    language = models.ForeignKey(Language,on_delete = models.SET_NULL, null = True)
    service = models.ForeignKey(VoiceService, on_delete = models.CASCADE)
    

    class Meta:
        verbose_name = _('Caller')

    def __str__(self):
        if not (self.first_name or self.last_name):
            return "%s" % self.caller_id
        else:
            return "%s %s (%s)" % (self.first_name, self.last_name, self.caller_id)


def lookup_kasadaka_user_by_caller_id(caller_id, service):
    """
    If user with caller_id for current voice_service exists, returns User object.
    If user does not exist or caller_id is None, returns None.
    """
    if caller_id:
        try:
            return KasaDakaUser.objects.get(caller_id = caller_id,
                                      service = service)
        except KasaDakaUser.DoesNotExist:
            return None
    return None
