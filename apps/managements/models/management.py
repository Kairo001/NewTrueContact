# Django
from django.db import models
from django.utils.translation import gettext as _

# Base model
from apps.base.models import BaseModel

# Campaign model
from apps.campaigns.models import Campaign

# User model
from apps.users.models import User, UserProfile

class TypeManagement(models.Model):
  """Model definition for TypeManagement."""

  name = models.CharField(_("name"), max_length=50)  

  class Meta:
    """Meta definition for TypeManagement."""

    verbose_name = 'TypeManagement'
    verbose_name_plural = 'TypesManagement'

  def __str__(self):
    """Unicode representation of TypeManagement."""
    return self.name


class OriginManagement(models.Model):
  """Model definition for Origin."""

  name = models.CharField(_("name"), max_length=50)
  type = models.ForeignKey(TypeManagement, on_delete=models.PROTECT)

  class Meta:
    """Meta definition for Origin."""

    verbose_name = 'Origin'
    verbose_name_plural = 'Origins'

  def __str__(self):
    """Unicode representation of Origin."""
    pass

class Management(BaseModel):
  """Model definition for Management.
  
  A management is a record that contains the result of a request or request from a client.
  """

  STATE_CHOICES = (
    ('in_process', 'In process'),
    ('finished', 'Finished'),
  )

  campaign = models.ForeignKey(Campaign, on_delete=models.PROTECT)
  agent = models.ForeignKey(User, on_delete=models.PROTECT)
  client = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
  metadata = models.TextField(help_text=_("Data about the data originated only in telephony management."))
  status = models.CharField(_("management status"), max_length=15, choices=STATE_CHOICES)
  origin = models.ForeignKey(OriginManagement, on_delete=models.PROTECT)

  class Meta:
    """Meta definition for Management."""

    verbose_name = 'Management'
    verbose_name_plural = 'Managements'

  def __str__(self):
    """Unicode representation of Management."""
    pass
