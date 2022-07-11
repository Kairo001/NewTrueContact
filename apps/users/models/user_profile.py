
# Django
from django.db import models
from django.utils.translation import gettext as _

# Base model
from apps.base.models import BaseModel

# User Model
from django.contrib.auth import get_user_model
User = get_user_model()

class UserProfile(BaseModel):
  """Model definition for UerProfile.
  
  The instances of this model will be the contacts or clients of the company and will also be the profiles of the users of the platform.
  """

  first_name = models.CharField(_("First name"), max_length=64)
  last_name = models.CharField(_("Last name"), max_length=64)
  document = models.CharField(_("Document"), max_length=20, blank=True, null=True)
  image = models.ImageField(_('Profile picture'), upload_to='profile_pictures/', blank=True, null=True)

  agent = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

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
    return f'{self.first_name} {self.last_name}'

  def get_profile_data(self):
    """Method to get all profile data."""
    return list(self.data.filter(is_active=True).values('label__name', 'type__name', 'data'))