# Django
from django.db import models
from django.utils.translation import gettext as _

# Management model
from apps.managements.models import Management

# FormField moel
from apps.campaigns.models import FormField

class DataField(models.Model):
  """Model definition for DataField."""

  management = models.ForeignKey(Management, on_delete=models.PROTECT, related_name="data_fields")
  form_field = models.ForeignKey(FormField, on_delete=models.PROTECT)
  data = models.CharField(_("field data"), max_length=1024, blank=True, null=True)
  data_boolean = models.BooleanField(blank=True, null=True, help_text=_("Attribute that is used only when the field is checkbox type."))

  class Meta:
    """Meta definition for DataField."""

    verbose_name = 'DataField'
    verbose_name_plural = 'DataFields'

  def __str__(self):
    """Unicode representation of DataField."""
    pass
