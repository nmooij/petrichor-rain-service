from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext

from django.utils import timezone
from . import CallSession, VoiceService


class UserInputCategory(models.Model):
    name = models.CharField(_('Name'),max_length = 100, blank = False, null = False)
    description = models.CharField(_('Description'),max_length = 1000, blank = True, null = True)
    service = models.ForeignKey(VoiceService, on_delete=models.CASCADE, related_name="service", verbose_name = _('Voice service'))

    class Meta:
        verbose_name = _('User Input Category')

    def __str__(self):
        return '"%s" ("%s")'%(self.name, self.service.name)


class UserInput(models.Model):
    input_value = models.CharField(max_length = 100, blank = True, null = True, default='null')
    session = models.ForeignKey(CallSession, on_delete=models.CASCADE)
    category = models.ForeignKey(UserInputCategory, on_delete=models.CASCADE, verbose_name = _('Category'))
    input_description = models.CharField(max_length = 1000, blank = True, null = True, verbose_name = _('Description'), default='null')
    input_date = models.DateField(_('Input date'),auto_now_add = True)


class Meta:
    verbose_name = _('User Input')
