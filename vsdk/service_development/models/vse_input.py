from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext

from vsdk.service_development.models import VoiceLabel
from .vs_element import VoiceServiceElement
from .user_input import UserInputCategory

class InputData(VoiceServiceElement): 
    """
        An element that saves user input to a line in the database.
    """

    _urls_name = 'service-development:InputData'


    final_voice_label = models.ForeignKey(
        VoiceLabel,
        verbose_name = _('Final voice label'),
        help_text = _('The voice label that is played when the user has completed the input process. Example: "Thank you for your message! The message has been stored successfully."'),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='final_voice_label_input',
    )
    input_category = models.ForeignKey(
        UserInputCategory,
        verbose_name = _('Input category'),
        help_text = _('The category under which the input will be stored in the system.'),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='input_category_input',
    )
    

    _redirect = models.ForeignKey(
        VoiceServiceElement,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(app_label)s_%(class)s_related',
        verbose_name = _('Redirect element'),
        help_text=_("The element to redirect to after the message has been played."))

    class Meta:
        verbose_name = _('Input Element')

    @property
    def redirect(self):
        """
        Returns the actual subclassed object that is redirected to,
        instead of the VoiceServiceElement superclass object (which does
        not have specific fields and methods).
        """
        if self._redirect:
            return VoiceServiceElement.objects.get_subclass(id=self._redirect.id)
        else:
            return None

    def __str__(self):
        return "InputData: " + self.name

    def is_valid(self):
        return len(self.validator()) == 0
    is_valid.boolean = True
    is_valid.short_description = _('Is valid')

    def validator(self):
        errors = []
        errors.extend(super(InputData, self).validator())
        if not self._redirect:
            errors.append(ugettext('Input does not have a redirect element') % self.name)
        return errors

