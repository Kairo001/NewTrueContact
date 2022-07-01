
# Django
from django.db import models
from django.utils.translation import gettext as _

# Base model
from apps.base.models import BaseModel

class UserProfile(BaseModel):
  """Model definition for UerProfile."""

  first_name = models.CharField(_("First name"), max_length=64)
  last_name = models.CharField(_("Last name"), max_length=64)
  document = models.CharField(_("Document"), max_length=20, blank=True, null=True)

  class Meta:
    """Meta definition for UerProfile."""
    verbose_name = 'UserProfile'
    verbose_name_plural = 'UserProfiles'

  def __str__(self):
    """Unicode representation of UserProfile."""
    return self.first_name

  def get_short_name(self):
    """Method to get the first name of the user."""
    self.first_name

  def get_full_name(self):
    """Method to get the full name of the user."""