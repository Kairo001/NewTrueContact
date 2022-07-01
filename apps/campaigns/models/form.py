# Django
from django.db import models
from django.utils.translation import gettext as _

# Base model
from apps.base.models import BaseModel

class Form(BaseModel):
  """Model definition for Form.

  A form is the information placed by the agent for each of the user management. Each campaign has its respective form.
  """

  name = models.CharField(_("name"), max_length=50)
  description = models.TextField(_("description"))

  class Meta:
    """Meta definition for Form."""

    verbose_name = 'Form'
    verbose_name_plural = 'Forms'

  def __str__(self):
    """Unicode representation of Form."""
    self.name

class FormField(BaseModel):
  """Model definition for FieldForm.
  
  A form field is one of the custom fields that this form will have.
  """

  TYPE_CHOICES = (
    ('text', 'Text'),
    ('date', 'Date'),
    ('datetime-local', 'Datetime'),
    ('textarea', 'Text area'),
    ('select', 'Select'),
    ('number', "Number"),
    ('checkbox', 'Check box'),
    ('time', 'Time'),
  )

  form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name="fields")
  name = models.CharField(_("name"), max_length=252)
  tipo = models.PositiveIntegerField(_("field type"), choices=TYPE_CHOICES)
  values_select = models.TextField(_("Values of select"),blank=True, null=True, help_text=_("This parameter is required when the field is of type select."))
  is_required = models.BooleanField(_("Required field?"))

  class Meta:
    """Meta definition for FieldForm."""

    verbose_name = 'FieldForm'
    verbose_name_plural = 'FieldsForm'

  def __str__(self):
    """Unicode representation of FieldForm."""
    return self.name