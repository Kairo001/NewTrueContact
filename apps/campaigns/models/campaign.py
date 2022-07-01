# Django
from django.db import models
from django.utils.translation import gettext as _

# Base model
from apps.base.models import BaseModel

# User model
from apps.users.models import User

# Form model
from apps.campaigns.models import Form

class Campaign(BaseModel):
  """Model definition for Campaign.
  
  A campaign is the way to encapsulate or group the operations within the company. Example: Customer service, Sales...
  """

  name = models.CharField(_("name"), max_length=50)
  form = models.ForeignKey(Form, on_delete=models.PROTECT)
  users = models.ManyToManyField(User)

  class Meta:
    """Meta definition for Campaign."""

    verbose_name = 'Campaign'
    verbose_name_plural = 'Campaigns'

  def __str__(self):
    """Unicode representation of Campaign."""
    return self.name
